from os import walk
from InvertedIndexGenerator import create_token_tuples,create_posting_lists


def get_fileNames():
    f = []
    for (dirpath, dirnames, filenames) in walk("C:\\Users\\capiot\\Desktop\\InvertedIndexDRS\\Corprus"):
        f.append(filenames)
    return f

def create_input_param(f):
    wordList = []
    for fileNames in f:
        for files in fileNames:
           fileName = 'C:\\Users\\capiot\\Desktop\\InvertedIndexDRS\\Corprus\\' + files
           f = open(fileName)
           lines = f.readlines()
           for words in lines:
                wordList.append(words)
           f.close()
    return wordList

f = []
f = get_fileNames()

file_map = {}
index = 0
for file in f:
    for fileNames in file:
        file_map[index] = fileNames
        index += 1
print(file_map)

token_tuple_list = create_token_tuples(create_input_param(f))
map = create_posting_lists(token_tuple_list)

print(map)

def get_files(word):
    print("Word : " + word + " is present in following files")
    try:
        for file_index in map[word]:
            print(file_map[file_index])
    except:
        print("Word not present in any of the files")

get_files('Sampl'.lower())


