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
            self.tags = set([key for key in frequencies.keys() if frequencies[key] >= filter_freq])

    def save(self, output_path):
        with open(output_path, 'wb') as f:
            pickle.dump(self, f)

    def tagged_as(self, tags, name=None, export=False):
        result = list(map(lambda x: x[0], filter(lambda x: x[1] in tags, self.tags)))
        if result and export:
            output_path = (name if name else '_'.join(tags)) + '.txt'
            with open(output_path, 'w', encoding='utf-8') as fp:
                for item in result:
                    fp.write("%s\n" % item)
        return result

    @staticmethod
    def load(input_path):
        with open(input_path, 'rb') as f:
            return pickle.load(f)
