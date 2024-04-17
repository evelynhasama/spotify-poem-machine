import nltk
import collections
import random

nltk.download('punkt')  # Download the Punkt Tokenizer Models
nltk.download('averaged_perceptron_tagger')  # Download the POS Tagging Model


def create_poem(tracks_data):
    pos_arrays = collections.defaultdict(list)
    for track in tracks_data:
        tokens = nltk.word_tokenize(track)
        pos_words = nltk.pos_tag(tokens)
        for word, tag in pos_words:
            if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
                pos_arrays['nouns'].append(word)
            elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                pos_arrays['verbs'].append(word)
            elif tag in ['JJ', 'JJR', 'JJS']:
                pos_arrays['adjectives'].append(word)
            elif tag in ['RB', 'RBR', 'RBS']:
                pos_arrays['adverbs'].append(word)
            else:
                pos_arrays['other'].append(word)
    
    poem = []
    constructions = [("nouns", "verbs"), ("nouns", "verbs", "nouns"), ("nouns", "verbs", "adverbs")]
    
    for _ in range(10):
        construction_index = random.randint(0, len(constructions) - 1)
        new_line = []
        for part in constructions[construction_index]:
            if part in pos_arrays:
                new_line.append(random.choice(pos_arrays[part]))
        poem.append(' '.join(new_line))

    return poem