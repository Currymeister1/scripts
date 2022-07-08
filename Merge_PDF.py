# Importing useful modules
import sys
from PyPDF2 import PdfFileMerger


pdf_merger = PdfFileMerger()

input_files = []

# Getting the input files from the command line
for arg in sys.argv[1:len(sys.argv)-1]:
   input_files.append(arg)

# Getting the name of output file from the command line
out_file_name = sys.argv[-1]


# Merging the files
for file in input_files:
    try:
        pdf_merger.append(file)
    except Exception:
        print("Please Provide PDFs Only!")
        sys.exit(1)


# Saving the result into the output file
try:
    pdf_merger.write(out_file_name)
except Exception:
    print('The name for the output file already exists! Please pick a different name')
    sys.exit(1)

pdf_merger.close()