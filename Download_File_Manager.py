# Importing useful modules 
from os import listdir
from os.path import isfile, join
import os


# Getting the path
mypath = os.path.expanduser('~/Downloads')
# Listing the files in the Download directory
onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]


# Print for testing
print(onlyfiles)