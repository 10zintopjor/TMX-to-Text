from translate.storage.tmx import tmxfile
from pathlib import Path
from bs4 import BeautifulSoup

def parse_segment(multilingual_segment):
    segments = multilingual_segment.find_all('term')
    global src_seg,tar_teg
    for segment in segments:
        seg_text = segment.text if segment.text else '-----'
        if segment.get("xml:lang", "") == "bo":
            src_seg = seg_text.strip() 
        elif segment.get("xml:lang", "") == "" and segment.get("type", "") == "": 
            tar_seg = seg_text.strip()
            
    
    tar = ' '.join(tar_seg.replace("\n","").split())
    line =src_seg+" @ "+tar
    return line

def parse_xml(xml_content):
    lines = ''
    soup = BeautifulSoup(xml_content, "xml")
    multilingual_segments = soup.find_all("gloss")
    for multilingual_segment in multilingual_segments:
        line = parse_segment(multilingual_segment)
        lines += line+"\n"
    return lines

def remove_duplicates(dict):

    file = open(dict)
    l = set(file.readlines())
    file.close()

    file = open(dict,"w")
    
    for x in l:
        y = x
        file.write(y)
    file.close()    


if __name__ == "__main__":
    text_paths = list(Path('./translations/').iterdir())
    text_paths.sort()
    dict = "bo-en.dic"
    f = open(dict,"a")
    for text_path in text_paths:
        xml = text_path.read_text(encoding='utf-8')
        lines = parse_xml(xml)
        f.write(lines)
    f.close()
    remove_duplicates(dict)
        