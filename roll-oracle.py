import random
import sys
import pickle


def entries(taggings, keys):
  categories = [taggings[key] for key in keys]
  categories = [element for category in categories for element in category]
  return list(set(categories))


def roll(type, *entries):
  rolls = [random.choice(entry) for entry in entries]
  concat = ' '.join(rolls)
  print(f'{type}: {concat}')


inputFile = sys.argv[1]
taggings = {}
with open(inputFile, 'rb') as f:
    taggings = pickle.load(f)

action1 = entries(taggings, ['VB', 'VBP'])
action2 = entries(taggings, ['NN', 'NNS', 'NNP'])
desc1 = entries(taggings, ['RB'])
desc2 = entries(taggings, ['JJ', 'VBN', 'VBD'])

for i in range(0, 5): roll('Action', action1, action2)

print('\n')

for i in range(0, 5): roll('Description', desc1, desc2)
