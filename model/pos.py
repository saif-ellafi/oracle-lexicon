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
        self.tags = set([element for sublist in tags for element in sublist])

    def save(self, output_path):
        with open(output_path, 'wb') as f:
            pickle.dump(self, f)

    def tagged_as(self, tags):
        return list(map(lambda x: x[0], filter(lambda x: x[1] in tags, self.tags)))

    @staticmethod
    def load(input_path):
        with open(input_path, 'rb') as f:
            return pickle.load(f)
