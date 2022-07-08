# Some Python Scripts

Just trying out python and automating process to boost productivity ;)

## Download File Manager
Sorting the files in Download folder into different sub folders based on the file type. Currently, there are four sub categories:    
1. PDFs 
2. Images (jpeg, png)
3. Videos (mp4, mov, wmv, avi, gif)
4. Documents (doc, docx, odt, rtf, tex, txt, wpd)  

For windows users: You need to change the myPath variable.



### How To Automatically Run The Script
You can use incrontab, which is available on most linux distors ([Arch Wiki](https://wiki.archlinux.org/title/Incron)). You will need **IN_CREATE** and **IN_MOVE_TO**  mask types. 

## Merge PDF
Merging arbitary PDFs into a one single PDF. To use this script: `python3 Merge_PDF.py input_file_1.pdf input_file_2.pdf .. input_file_n.pdf output_file.pdf` or if you want merge all PDFs in a directory, then use: `python3 Merge_PDF.py *.pdf output_file.pdf`.  
**Note**: If a file is already using a same name as the output file, then you have to use a different name. 

## PNG_To_PDF
**Imagine this**: You are doing an online exam and it's about to scan your solutions. You use windows in-built scanner programm and instead of getting PDF, you  
get a lot of images. The time is ticking and you have to convert these images into a single PDF. How can you do this quickly?   

**Easy**: By using this awesome script. `python3 PNG_To_PDF -s image_1.jpg image_2.jpg .. image_n.jpg -o solutions.pdf`.    
The -s flag sorts the images and -o flag is for naming the output file. By default the name of the outfile be result.pdf