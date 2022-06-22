import pickle
import random
import sys


def pos_format(tags, keys):
    categories = [tags[key] for key in keys]
    categories = [element for category in categories for element in category]
    return list(set(categories))


def roll(label, *entries):
    rolls = [random.choice(entry) for entry in entries]
    concat = ' '.join(rolls)
    print(f'{label}: {concat}')


inputFile = sys.argv[1]
with open(inputFile, 'rb') as f:
    tagged_words = pickle.load(f)

action1 = pos_format(tagged_words, ['VB', 'VBP'])
action2 = pos_format(tagged_words, ['NN', 'NNS', 'NNP'])
desc1 = pos_format(tagged_words, ['RB'])
desc2 = pos_format(tagged_words, ['JJ', 'VBN'])

for i in range(0, 5):
    roll('Action', action1, action2)

print('\n')

for i in range(0, 5):
    roll('Description', desc1, desc2)
