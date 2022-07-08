import argparse
from PIL import Image


parser = argparse.ArgumentParser(description='Add Images To Merge Into A Single PDF')
parser.add_argument('--s','--sort',dest='sort',help='Sort the input files')
parser.add_argument('files',nargs='*')

args = parser.parse_args()


output = []
files = []

for arg in args.files:
    files.append('%s'%(arg))

if args.sort:
    files.sort()

# Testing
for file in files:
    img = Image.open(file)
    im = img.convert('RGB')
    output.append(im)

output[0].save(r'./my_images.pdf', save_all=True, append_images=output[1:])