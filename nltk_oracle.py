import pickle
import random
import sys

import data.input
import model.sentence
import model.token
import model.pos

import nltk

NLTK_MODELS = [
    'averaged_perceptron_tagger',
    'punkt',
    'stopwords',
    'universal_tagset',
    'universal_treebanks_v20',
    'wordnet2021'
    ]


def models():
    for pretrained in NLTK_MODELS:
        nltk.download(pretrained)


def load(input_file):
    with open(input_file, 'rb') as f:
        pos_tagger = pickle.load(f)
    return pos_tagger


def parse(text):
    cleaned = data.input.cleanup_breaklines(text)
    corrected = data.input.cleanup_characters(cleaned)
    sentences = model.sentence.extract_sentences(corrected)
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.append(model.token.tokenize_sentence(sentence))
    return model.pos.NLTKPosTagger(tokenized_sentences)


def parse_txt(path):
    return parse(data.input.load_txt(path))


def parse_pdf(path, page_start, page_end):
    return parse(data.input.load_pdf(path, page_start, page_end))


def gen(pos_tagger):
    def roll(label, *entries):
        rolls = [random.choice(entry) for entry in entries]
        concat = ' '.join(rolls)
        print(f'{label}: {concat}')

    action1 = pos_tagger.tagged_as(['VB', 'VBP'])
    action2 = pos_tagger.tagged_as(['NN', 'NNS', 'NNP'])
    desc1 = pos_tagger.tagged_as(['RB'])
    desc2 = pos_tagger.tagged_as(['JJ', 'VBN'])

    for i in range(0, 5):
        roll('Action', action1, action2)

    print('')

    for i in range(0, 5):
        roll('Description', desc1, desc2)


"""
USAGE:
python ./nltk_oracle.py parse path/to/file.txt
python ./nltk_oracle.py save path/to/file.txt path/to/output.pickle
python ./nltk_oracle.py load path/to/output.pickle
python ./nltk_oracle.py parse path/to/file.pdf 10 15
python ./nltk_oracle.py save path/to/file.pdf 10 15 path/to/output.pickle
"""


def __main__():
    action = sys.argv[1]
    input_path = sys.argv[2]
    if action == 'parse':
        if input_path.endswith('.txt'):
            gen(parse_txt(input_path))
        elif input_path.endswith('.pdf'):
            gen(parse_pdf(input_path, sys.argv[3], sys.argv[4]))
        else:
            raise Exception('Supported either .txt or .pdf input paths')
    elif action == 'save':
        if input_path.endswith('.txt'):
            parse_txt(input_path).save(sys.argv[3])
        elif input_path.endswith('.pdf'):
            parse_pdf(input_path, sys.argv[3], sys.argv[4]).save(sys.argv[5])
        else:
            raise Exception('Supported either .txt or .pdf input paths')
    elif action == 'load':
        gen(load(sys.argv[2]))
    else:
        raise Exception('Supported action either parse, save or load')
