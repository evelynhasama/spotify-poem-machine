from flask import Flask, redirect, request, session, render_template, make_response, url_for
import spotipy
import keys
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = keys.secret_key

# Define your Spotify API credentials
CLIENT_ID = keys.client_id
CLIENT_SECRET = keys.client_secret
REDIRECT_URI = 'http://localhost:3000/callback'

# Scope for user's top tracks
SCOPE = 'user-top-read'

@app.route('/clear-cache')
def clear_cache():
    response = make_response('Cache cleared')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'token_info' in session:
            term = request.form.get('term')
            amount = request.form.get('amount')
            return redirect(url_for('top_tracks', term=term, amount=amount))
    else:
        if 'token_info' in session:
            return render_template('home.html', logged_in=True)
        else:
            return render_template('home.html', logged_in=False)

@app.route('/login')
def login():
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)

    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)

    auth_token = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = auth_token

    return redirect('/')

@app.route('/top_tracks')
def top_tracks():
    if 'token_info' not in session:
        return redirect('/login')

    token_info = session['token_info']
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    time_range = request.args.get('term')
    limit = int(request.args.get('amount'))

    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    
    poem_title = "Confessions from the"
    if time_range == 'short_term':
        poem_title += " Last 4 Weeks"
    elif time_range == 'medium_term':
        poem_title += " Last 6 Months"
    elif time_range == 'long_term':
        poem_title += " Last 1 Year"
    

    tracks_data = []
    for track in top_tracks['items']:
        tracks_data.append({
            'name': track['name'].lower()
        })

    return render_template('poem.html', tracks_data=tracks_data, poem_title=poem_title)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)