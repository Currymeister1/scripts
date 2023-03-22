import sys

files_from_arguments = sys.argv[1:]

dummy_text = files_from_arguments[0]
replace_word_list = files_from_arguments[1]


def count_replace_str(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        content = file.read()
        for words in content.split():
            if word in words:
                count+=1
    return count

def read_replace_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content.split(";")

count = count_replace_str(files_from_arguments[0], '$REPLACE')
replace_list = read_replace_words(replace_word_list)

if(count != len(replace_list)):
    print("Replacing words count mismatch")
    sys.exit()

with open(dummy_text, "rt") as fin:
    with open("out.txt", "wt") as fout:
        i = 0
        for line in fin:
                if("$REPLACE" in line):
                    fout.write(line.replace("$REPLACE", replace_list[i]))
                    i+=1
                else:
                    fout.write(line)
            
            