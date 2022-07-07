# Importing useful modules 
from os import listdir
from os.path import isfile, join
import os
import shutil



imageExtensions = ['jpeg','png','jpg']

# Getting the path
mypath = os.path.expanduser('~/Downloads')
# Listing the files in the Download directory
onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]


newFolders = ['Images', 'PDFs', 'Videos', 'Docs']

# check if the new directories already exist
for folders in newFolders:
    newPath = mypath+'/'+folders
    if(not os.path.exists(newPath)):
        os.mkdir(newPath)
    else:
        print("%s already exists" % folders)


# Moving the files
for file in onlyfiles:
    extensions = os.path.splitext(file)[1][1:]
    currPath = mypath+'/'+file
    print(extensions)
    if(extensions == 'pdf'):
        destPath = mypath+'/'+newFolders[1]
        shutil.move(currPath,destPath)
    if(extensions in imageExtensions):
        destPath = mypath+'/'+newFolders[0]
        shutil.move(currPath,destPath)
    



# Print for testing
print(newFolders)