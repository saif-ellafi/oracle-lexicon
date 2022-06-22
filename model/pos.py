import nltk
import pickle

"""
IMPLEMENT ALL POS TAGGERS HERE
"""


class NLTKPosTagger:
    def __init__(self, tokenized_sentences):
        tags = []
        for words_list in tokenized_sentences:
            tags.append(nltk.pos_tag(words_list))
        self.tags = [element for sublist in tags for element in sublist]

    def save(self, output_path):
        with open(output_path, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(input_path):
        with open(input_path, 'rb') as f:
            return pickle.load(f)
