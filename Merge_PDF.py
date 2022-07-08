import sys
from PyPDF2 import PdfFileMerger


pdf_merger = PdfFileMerger()

input_files = []


for arg in sys.argv[1:]:
   input_files.append(arg)


for file in input_files:
    pdf_merger.append(file)

pdf_merger.write('result.pdf')
pdf_merger.close()