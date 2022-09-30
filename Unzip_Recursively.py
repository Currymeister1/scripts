from os import listdir
import os
from zipfile import ZipFile, is_zipfile

# Current Directory
mypath = os.getcwd()


# Extraction happens here and a new folder is created
def extractor(file):
    with ZipFile(file) as zipObj:
        print('Unzipping now: ', zipObj.filename)
        path = os.path.splitext(file)[0]
        zipObj.extractall(path)
        #os.remove(file)
        caller(path)


def caller(path):
    for file in listdir(path):
        complete_path = os.path.join(path,file)
        if(is_zipfile(complete_path)):
            extractor(complete_path)


caller(mypath)


