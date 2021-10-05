import spacy
from pathlib import Path


def tokenize_line(line, nlp):
    normalized_line = ''
    doc = nlp(line)
    for token in doc:
        if token.is_punct:
            continue
        normalized_line += f'{token.lemma_.lower()} '
    normalized_line = normalized_line.strip()
    return normalized_line + '\n'


def tokenize_text(text, nlp):
    tokenized_text = ''
    lines = text.splitlines()
    for line in lines:
        tokenized_text += tokenize_line(line,nlp)
    return tokenized_text


if __name__ == "__main__":
    text_paths = list(Path('./en_text/').iterdir())
    text_paths.sort()
    nlp = spacy.load('en_core_web_sm')
    corpus = ''
    for text_path in text_paths[:2]:
        text = text_path.read_text(encoding='utf8')
        corpus += tokenize_text(text,nlp)
        print(text_path.stem)
    Path('./en_corpus.txt').write_text(corpus, encoding='utf-8')


    

