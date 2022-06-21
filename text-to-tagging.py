import nltk
import pickle
import sys

for d in ['averaged_perceptron_tagger', 'punkt', 'stopwords', 'universal_tagset', 'universal_treebanks_v20', 'wordnet2021']:
  nltk.download(d)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

inputFile = sys.argv[1]
outputFile = sys.argv[2]

stop_words = set(stopwords.words('english'))
text=''
with open(inputFile, 'r') as f:
  text=f.read()

sentences = sent_tokenize(text)

pos_tags = []
for sentence in sentences:
    wordsList = word_tokenize(sentence)
    wordsList = [w for w in wordsList if not w in stop_words]
    pos_tags.append(nltk.pos_tag(wordsList))
 
pos_tags = [element for sublist in pos_tags for element in sublist]

taggings = defaultdict(list)
for v, k in pos_tags: taggings[k].append(v)

with open(outputFile, 'wb') as f:
    pickle.dump(taggings, f)