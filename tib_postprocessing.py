from botok.modifytokens.splitaffixed import split_affixed
from botok.tokenizers.wordtokenizer import WordTokenizer
from pathlib import Path


def tokenize_line(line, wt):
    """tokenize word from line

    Args:
        line (str): line from a para
        wt (obj): word tokenizer objet

    Returns:
        str: tokenized line
    """
    new_line = ''
    tokens = wt.tokenize(line, split_affixes=False)
    for token in tokens:
        new_line += f'{token.text} '
    new_line = new_line.replace('!', '')
    return new_line

def tokenize_text(text, wt):
    new_text = ''
    lines = text.splitlines()
    for line in lines:
        new_text += tokenize_line(line, wt) + '\n'
    return new_text


if __name__ == "__main__":
    wt = WordTokenizer()
    text_paths = list(Path('./bo_text/').iterdir())
    text_paths.sort()
    tokenized_text = ''
    for text_path in text_paths:
        text = text_path.read_text(encoding='utf8')
        tokenized_text += tokenize_text(text, wt)
    Path(f'./tokenize_bo_text/{text_path.stem}.txt').write_text(tokenized_text)
    # text = Path('./bo_text/bo_001.txt').read_text(encoding='utf-8')
    # new_text = tokenize_text(text, wt)
    # Path('./bo_t.txt').write_text(new_text, encoding='utf-8')