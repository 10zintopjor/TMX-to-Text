import logging
from botok.modifytokens.splitaffixed import split_affixed
from botok.tokenizers.wordtokenizer import WordTokenizer
from pybo.utils.regex_batch_apply import batch_apply_regex, get_regex_pairs
from pathlib import Path
from horology import timed

logging.basicConfig(filename="bo_norm.log", level=logging.DEBUG, filemode="w")

def tokenize_line(line, wt, rules):
    """tokenize word from line

    Args:
        line (str): line from a para
        wt (obj): word tokenizer objet

    Returns:
        str: tokenized line
    """
    new_line = ''
    tokens = wt.tokenize(line, split_affixes=True)
    for token in tokens:
        # if token.pos == "PUNCT" or token.pos == "PART" or token.chunk_type == 'PUNCT':
        if token.pos == "PUNCT" or token.chunk_type == 'PUNCT':
            continue
        new_line += f'{token.lemma} '
        # new_line += f'{token.text} '
    new_line = new_line.strip()
    normalized_line = normalize_line(new_line, rules)
    return normalized_line

@timed(unit='min', name='Tokenizing took ')
def tokenize_text(text_name, text, wt, rules):
    new_text = ''
    lines = text.splitlines()
    for line in lines:
        new_text += tokenize_line(line, wt, rules) + '\n'
    logging.info(f'Number of lines in text {text_name} is {len(lines)}')
    return new_text

def normalize_line(line, rules):
    normalized_line = batch_apply_regex(line, rules)
    return normalized_line

if __name__ == "__main__":
    wt = WordTokenizer()
    text_paths = list(Path('./bo_text/').iterdir())
    text_paths.sort()
    tokenized_text = ''
    regex_file = Path('./regex.txt')
    rules = get_regex_pairs(regex_file.open(encoding="utf-8-sig").readlines())
    for text_path in text_paths:
        text = text_path.read_text(encoding='utf8')
        tokenized_text += tokenize_text(text_path.stem, text, wt, rules)
    # Path(f'./normalized/bo/bo_corpus-punct-part_lemma.txt').write_text(tokenized_text)
    # Path(f'./normalized/bo/bo_corpus-punct-part_text.txt').write_text(tokenized_text)
    Path(f'./normalized/bo/bo_corpus-punct_text.txt').write_text(tokenized_text)
    # Path(f'./normalized/bo/bo_corpus-punct_lemma.txt').write_text(tokenized_text)