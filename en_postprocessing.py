import spacy
from pathlib import Path

def tokenize(text,f):
    nlp = spacy.load('en_core_web_sm')
    nlp.max_length = 1930000
    doc = nlp(text) 

    for token in doc:
        if token.pos_ != "PUNCT":
            f.write(token.lemma_)
            if token.lemma_ != "\n":
                f.write(" ")

if __name__ == "__main__":
    text_paths = list(Path('./en_text/').iterdir())
    text_paths.sort()
    f = open('myfile.txt', 'a')
     
    for text_path in text_paths:
        text = text_path.read_text(encoding='utf8')
        tokenize(text,f)



    

