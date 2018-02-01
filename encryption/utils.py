import json

def get_english_dictionary():
    with open('data/words_dictionary.json', 'r') as infile:
        english_dictionary = json.loads(infile.read())
        return english_dictionary

def get_text_as_string(file_name):
    with open('data/{}.txt'.format(file_name), 'r') as infile:
        return infile.read()