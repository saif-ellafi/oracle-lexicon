import pickle
import random
import argparse

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

parser = argparse.ArgumentParser(description='Oracle Lexicon Builder')
parser.add_argument('action', type=str, help='parse|save|load')
parser.add_argument('path',  type=str, help='file path to source or pickle')
parser.add_argument('--pdf-range', type=str, help='Page Range for PDF files, comma separated i.e. 182,365')
parser.add_argument('--min-freq', type=int, default=1, help='Minimum frequency of words. Default 2')
parser.add_argument('--name', type=str, default='proj', help='Project name, used for output files')
parser.add_argument('--export', action='store_true', help='Project name, used for output files')


def models():
    for pretrained in NLTK_MODELS:
        nltk.download(pretrained)


def load(input_file):
    with open(input_file, 'rb') as f:
        pos_tagger = pickle.load(f)
    return pos_tagger


def parse(text, min_freq=1):
    cleaned = data.input.cleanup_breaklines(text)
    corrected = data.input.cleanup_characters(cleaned)
    sentences = model.sentence.extract_sentences(corrected)
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.append(model.token.tokenize_sentence(sentence))
    return model.pos.NLTKPosTagger(tokenized_sentences, min_freq)


def parse_txt(path, min_freq=1):
    return parse(data.input.load_txt(path), min_freq)


def parse_pdf(path, page_start, page_end, min_freq=1):
    return parse(data.input.load_pdf(path, page_start, page_end), min_freq)


def gen(pos_tagger, name, export):
    def roll(label, *entries):
        rolls = [random.choice(entry) for entry in entries]
        concat = ' '.join(rolls)
        print(f'{label}: {concat}')

    action1 = pos_tagger.tagged_as(['VB', 'VBP'], name+'_subject', export)
    action2 = pos_tagger.tagged_as(['NN', 'NNP'], name+'_action', export)
    desc1 = pos_tagger.tagged_as(['RB'], name+'_adverb', export)
    desc2 = pos_tagger.tagged_as(['JJ', 'VBN'], name+'_adjective', export)

    if action1 and action2:
        for i in range(0, 5):
            roll('Action', action1, action2)
    else:
        print('No Actions Vocabulary found!')

    print('')

    if desc1 and desc2:
        for i in range(0, 5):
            roll('Description', desc1, desc2)
    else:
        print('No Descriptions Vocabulary found!')


def main():
    args = vars(parser.parse_args())
    action = args['action']
    input_path = args['path']
    if action == 'parse':
        if input_path.endswith('.txt'):
            gen(parse_txt(input_path, args['min_freq']), args['name'], args['export'])
        elif input_path.endswith('.pdf'):
            page_range = args['pdf_range'].split(',')
            page_start = int(page_range[0])
            page_end = int(page_range[1])
            gen(parse_pdf(input_path, page_start, page_end, args['min_freq']), args['name'], args['export'])
        else:
            raise Exception('Supported either .txt or .pdf input paths')
    elif action == 'save':
        if input_path.endswith('.txt'):
            parse_txt(input_path, args['min_freq']).save(args['name'] + '.pickle')
        elif input_path.endswith('.pdf'):
            page_range = args['pdf_range'].split(',')
            page_start = int(page_range[0])
            page_end = int(page_range[1])
            parse_pdf(input_path, page_start, page_end, args['min_freq']).save(args['name'] + '.pickle')
        else:
            raise Exception('Supported either .txt or .pdf input paths')
    elif action == 'load':
        gen(load(args['path']), args['name'], args['export'])
    else:
        raise Exception('Supported action either parse, save or load')


"""
Example Usage
python nltk_oracle.py parse "path/to/book.pdf" --pdf-range 182,360 --min-freq 3 --export --name my_book
"""
if __name__ == "__main__":
    main()
