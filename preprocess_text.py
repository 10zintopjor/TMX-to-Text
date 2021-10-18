import re
from botok.tokenizers.wordtokenizer import WordTokenizer
from botok.tokenizers.sentencetokenizer import sentence_tokenizer
from pathlib import Path
from en_postprocessing import tokenize_line
from tib_postprocessing import normalize_line
from pybo.utils.regex_batch_apply import get_regex_pairs
import spacy

def get_tokens(text):
    wt = WordTokenizer()
    tokens = wt.tokenize(text, split_affixes=True)
    return tokens

def get_sentences(text):
    tokens = get_tokens(text)
    sentences = sentence_tokenizer(tokens)
    return sentences

def serialize_sentence(sentence, rules):
    new_line = ''
    for token in sentence:
        new_line += f'{token.text} '
    new_line = new_line.strip()
    normalized_line = normalize_line(new_line, rules)
    return normalized_line

def preprocess_bo_text(text, rules):
    new_bo_text = ''
    text = text.replace('\n', ' ')
    sentences = get_sentences(text)
    for sent_len, sentence in sentences:
        new_bo_text += serialize_sentence(sentence, rules) + '\n'
    return new_bo_text

def preprocess_en_text(text):
    new_eng_text = ''
    text = text.replace('\n', ' ')
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    for sentence in doc.sents:
        new_eng_text += sentence.text
    return new_eng_text

def preprocess_corpus(bo_text_path, en_text_path, rules):
    bo_text = Path(bo_text_path).read_text(encoding='utf-8')
    en_text = Path(en_text_path).read_text(encoding='utf-8')
    preprocess_bo = preprocess_bo_text(bo_text, rules)
    preprocess_en = preprocess_en_text(en_text)
    post_en_text_path = f'{en_text_path[:-4]}_norm.txt'
    post_bo_text_path = f'{bo_text_path[:-4]}_norm.txt'
    Path(post_bo_text_path).write_text(preprocess_bo, encoding='utf-8')
    Path(post_en_text_path).write_text(preprocess_en, encoding='utf-8')
    return [post_bo_text_path, post_en_text_path]


if __name__ == "__main__":
    regex_file = Path('./regex.txt')
    rules = get_regex_pairs(regex_file.open(encoding="utf-8-sig").readlines())
    bo_text_path = './test/bo_text/bo.txt'
    en_text_path = './test/en_text/en.txt'
    preprocess_corpus(bo_text_path, en_text_path, rules)
