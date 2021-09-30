from translate.storage.tmx import tmxfile
from pathlib import Path
from bs4 import BeautifulSoup

def parse_segment(multilingual_segment, src_lang, target_lang):
    src_seg = ''
    target_seg = ''
    segments = multilingual_segment.find_all('tuv')
    for segment in segments:
        seg_text = segment.find("seg").text if segment.find("seg").text else '-----'
        if segment.get("xml:lang", "") == src_lang:
            src_seg = seg_text.strip() + '\n'
        elif segment.get("xml:lang", "") == target_lang:
            target_seg = seg_text.strip() + '\n'
    return [src_seg, target_seg]

def parse_tmx(tmx_content, src_lang='bo', target_lang='en'):
    bi_text = {
        src_lang: '',
        target_lang: ''
    }
    soup = BeautifulSoup(tmx_content, "xml")
    multilingual_segments = soup.find_all("tu")
    for multilingual_segment in multilingual_segments:
        src_seg, tar_seg = parse_segment(multilingual_segment, src_lang, target_lang)
        bi_text[src_lang] += src_seg
        bi_text[target_lang] += tar_seg
    return bi_text


if __name__ == "__main__":
    tmx = Path('./tmx/sample.tmx').read_text(encoding='utf-8')
    bi_text = parse_tmx(tmx)
    Path('./bo_text/bo.txt').write_text(bi_text['bo'])
    Path('./en_text/en.txt').write_text(bi_text['en'])
    