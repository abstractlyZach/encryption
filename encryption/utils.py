import json

def get_english_dictionary():
    with open('data/words_dictionary.json', 'r') as infile:
        english_dictionary = json.loads(infile.read())
        return english_dictionary