# Importing useful modules 
from os import listdir
from os.path import isfile, join
import os


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





# Print for testing
print(newFolders)