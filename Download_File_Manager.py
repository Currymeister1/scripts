# Importing useful modules 
from os import listdir
from os.path import isfile, join
import os
import shutil


# Popular file types (add your desired file types here)
imageExtensions = ['jpeg','png','jpg','webp','svg']
videoExtensions = ['mp4','mov', 'wmv', 'avi','gif']
docsExtensions = ['odg','doc','docx','odt','rtf','tex','txt','wpd']
archiveExtensions = ['zip', 'rar']

# Getting the path
mypath = os.path.expanduser('~/Downloads')

# Listing the files in the Download directory
onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]


# Folders to be created 
newFolders = ['Images', 'PDFs', 'Videos', 'Docs','Archive']

# check if the new directories already exist
for folder in newFolders:
    newPath = mypath+'/'+folder
    if(not os.path.exists(newPath)):
        os.mkdir(newPath)
    


# Creating the destination path based on the file type
def destPathCreator():
    destPath = ''
    if(extensions in imageExtensions):
        destPath = mypath+'/'+newFolders[0]
    if(extensions == 'pdf'):
        destPath = mypath+'/'+newFolders[1] 
    if(extensions in videoExtensions):
        destPath = mypath+'/'+newFolders[2]
    if(extensions in docsExtensions):
        destPath = mypath+'/'+newFolders[3]
    if(extensions in archiveExtensions):
        destPath = mypath+'/'+newFolders[4]
    return destPath


# Moving the files
for file in onlyfiles:
    extensions = os.path.splitext(file)[1][1:]
    currPath = mypath+'/'+file
    destPath = destPathCreator()
    if(not destPath == ''):
        shutil.move(currPath,destPath)


