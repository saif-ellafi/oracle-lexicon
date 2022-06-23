import nltk
import pickle

"""
IMPLEMENT ALL POS TAGGERS HERE
"""


class NLTKPosTagger:
    def __init__(self, tokenized_sentences, filter_freq=1):
        tags = [nltk.pos_tag(words_list) for words_list in tokenized_sentences]
        flattened = [element for sublist in tags for element in sublist]
        if filter_freq == 1:
            self.tags = set(flattened)
        else:
            frequencies = {}
            for word in flattened:
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 0
            self.tags = [key for key in frequencies.keys() if frequencies[key] >= filter_freq]

    def save(self, output_path):
        with open(output_path, 'wb') as f:
            pickle.dump(self, f)

    def tagged_as(self, tags):
        return list(map(lambda x: x[0], filter(lambda x: x[1] in tags, self.tags)))

    @staticmethod
    def load(input_path):
        with open(input_path, 'rb') as f:
            return pickle.load(f)
