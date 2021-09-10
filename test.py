from translate.storage.tmx import tmxfile

with open("sample.tmx", 'rb') as fin:
    tmx_file = tmxfile(fin, 'bo','en')

filesrc = open("src.txt","a")
filetar = open("tar.txt","a")


for node in tmx_file.unit_iter():
    filesrc.writelines(node.source + "\n")
    filetar.writelines(node.target + "\n")


filesrc.close()
filetar.close()


