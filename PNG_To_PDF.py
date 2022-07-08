# Importing useful modules
import argparse
from PIL import Image
import sys

# Parsing the command line
parser = argparse.ArgumentParser(description='Add Images To Merge Into A Single PDF')
parser.add_argument('-s','--sort',dest='sort',action='store_true',help='Sort the input files')
parser.add_argument('files',nargs='*')
parser.add_argument('-o','--output',dest='output', help='Output file name')


args = parser.parse_args()


files = []
output = []

# Saving the image files into an array
for arg in args.files:
    files.append('%s'%(arg))

# If the sort flag is on, the array gets sorted
if args.sort:
    files.sort()

# Default name for the output file is result.pdf, but if the output flag is given, then use the user definied name
output_name = 'result.pdf'
if args.output:
    output_name = args.output

# Saving the images in an array
for file in files:
    try:
        img = Image.open(file)
        im = img.convert('RGB')
        output.append(im)
    except:
        print('Only Images Allowed!')
        sys.exit(1)

# Saving the output
try:
    output[0].save(output_name, save_all=True, append_images=output[1:])
except:
    print("File name should have the pdf extenstion!")