import spacy
from pathlib import Path
from horology import timed

def tokenize_line(line, nlp):
    normalized_line = ''
    doc = nlp(line)
    for token in doc:
        # if token.is_punct:
        if token.is_stop or token.is_punct:
            continue
        # normalized_line += f'{token.lemma_.lower()} '
        # normalized_line += f'{token.lower_} '
        normalized_line += f'{token.text} '
        # normalized_line += f'{token.norm_} '
    normalized_line = normalized_line.strip()
    return normalized_line + '\n'

@timed(unit='min', name='Tokenizing took ')
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
    for text_path in text_paths:
        text = text_path.read_text(encoding='utf8')
        corpus += tokenize_text(text,nlp)
        print(f'{text_path.stem} completed')
    # Path('./normalized/en/en_corpus-punct-stopword_lower.txt').write_text(corpus, encoding='utf-8')
    # Path('./normalized/en/en_corpus-punct-stopword_lemma_lower.txt').write_text(corpus, encoding='utf-8')
    # Path('./normalized/en/en_corpus-punct-stopword_norm.txt').write_text(corpus, encoding='utf-8')
    Path('./normalized/en/en_corpus-punct-stopword_text.txt').write_text(corpus, encoding='utf-8')
    # Path('./normalized/en/en_corpus-punct_text.txt').write_text(corpus, encoding='utf-8')
    # Path('./normalized/en/en_corpus-punct_lemma_lower.txt').write_text(corpus, encoding='utf-8')
    # Path('./normalized/en/en_corpus-punct_norm.txt').write_text(corpus, encoding='utf-8')


    

