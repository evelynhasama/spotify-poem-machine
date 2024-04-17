import nltk
import collections
import random
import re

nltk.download('punkt')  # Download the Punkt Tokenizer Models
nltk.download('averaged_perceptron_tagger')  # Download the POS Tagging Model


def create_poem(tracks_data):
    pos_arrays = collections.defaultdict(list)
    for track in tracks_data:
        track = expand_contractions(track)
        tokens = nltk.word_tokenize(track)
        pos_words = nltk.pos_tag(tokens)
        for word, tag in pos_words:
            if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
                pos_arrays['nouns'].append(word)
            elif tag in ['PRP', 'WP', 'WP$']:
                pos_arrays['pronouns'].append(word)
            elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                pos_arrays['verbs'].append(word)
            elif tag in ['JJ', 'JJR', 'JJS','PRP$']:
                pos_arrays['adjectives'].append(word)
            elif tag in ['RB', 'RBR', 'RBS']:
                pos_arrays['adverbs'].append(word)
            else:
                pos_arrays['other'].append(word)
    
    poem = []
    constructions = [("pronouns", "verbs"), ("nouns", "verbs"), ("pronouns", "verbs", "nouns"), ("adjectives", "nouns", "verbs"), ("nouns", "verbs", "nouns"), ("nouns", "verbs", "adverbs")]
    
    for _ in range(10):
        construction_index = random.randint(0, len(constructions) - 1)
        new_line = []
        for part in constructions[construction_index]:
            if part in pos_arrays:
                new_line.append(random.choice(pos_arrays[part]))
        poem.append(' '.join(new_line))

    return poem

    
contractions = {
    "ain't": "are not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it had",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there had",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have",
    "'s": "s",
}

def expand_contractions(text):
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    return text