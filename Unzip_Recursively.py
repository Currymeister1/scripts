from os import listdir
import os
from zipfile import ZipFile, is_zipfile

# Current Directory
mypath = '.'


def extractor(path):
    for file in listdir(path):
        if(is_zipfile(file)):
            print(file)
            with ZipFile(file) as zipObj:
                path = os.path.splitext(file)[0]
                os.makedirs(path)
                zipObj.extractall(path)
                os.chdir(path)
                extractor('.')

extractor(mypath)
