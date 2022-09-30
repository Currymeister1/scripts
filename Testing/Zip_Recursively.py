from os import listdir
import os
from zipfile import ZipFile, is_zipfile

# Current Directory
mypath = '.'
print(mypath)
'''
def zipper(path):
    files = []
    for file in listdir(path):
        if(os.path.isdir(os.path.join(path,file))):
            files.append(file)
            zipper(os.path.join(path,file))
        else:
            files.append(file)
    zipName = path+'.zip'
    zipObj = ZipFile(zipName,'w')
    for file in files:
        zipObj.write(path,os.path.basename(path)+'/'+file)
    zipObj.close()
'''

def zipper(path):
    for file in listdir(path):
        if(os.path.isdir(os.path.join(path,file))):
            zipper(os.path.join(path,file))
            print('Foler: ',path,'File: ',file)

            



zipper(mypath)