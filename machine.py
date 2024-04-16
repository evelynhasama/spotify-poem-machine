import spotipy
import keys
from spotipy.oauth2 import SpotifyOAuth

# Define your Spotify API credentials
CLIENT_ID = keys.client_id
CLIENT_SECRET = keys.client_secret
REDIRECT_URI = "http://localhost:3000"

# Scope for user's top tracks
SCOPE = 'user-top-read'

def get_user_top_tracks(time_range='short_term', limit=10):
    """
    Retrieves the user's top tracks.

    Parameters:
        time_range (str): The time range of top tracks. Possible values: 'short_term', 'medium_term', 'long_term'.
        limit (int): The maximum number of tracks to retrieve.

    Returns:
        list: A list of dictionaries representing the user's top tracks.
    """
    
    # Initialize Spotify API client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

    # Get user's top tracks
    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)

    return top_tracks['items']

def main():
    
    # asks users for what how recent of a confession they want to see
    time_range = input("\nHow recent do you want to see the confessions? \n1: short term \n2: medium term \n3: long term \n\n")
    
    title = ""
    track_limit = 0
    
    while time_range not in ['1', '2', '3']:
        time_range = input("Please enter a valid option: ")
        
    if time_range == '1':
        time_range = 'short_term'
        title = "Confessions from the Last 4 Weeks"
        track_limit = 10
    elif time_range == '2':
        time_range = 'medium_term'
        title = "Confessions from the Last 6 Months"
        track_limit = 15
    else:
        time_range = 'long_term'
        title = "Confessions from the Last Year"
        track_limit = 20

    
    # Get user's top tracks
    top_tracks = get_user_top_tracks(time_range=time_range, limit=track_limit)

    # Display user's top tracks
    print("\n" + title)
    print("by Evelyn Hasama \n")
    
    for i, track in enumerate(top_tracks, start=1):
        # prints each track on a new line
        print(track["name"].lower())

if __name__ == "__main__":
    main()
