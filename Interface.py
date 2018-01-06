from os import walk
from InvertedIndexGenerator import create_token_tuples,create_posting_lists


class Maps():
    def __init__(self):
        self.file_map = {}
        self.word_map = {}

def get_fileNames(dirName):
    """
    :param dirName: gives Name of the directory as input(Ex: C:/Users/capiot/Desktop/InvertedIndexDRS/Corpus)
    :return: files inside the directory (Sample1-Copy(3).txt,Sample2-Copy(4).txt,....)
    """
    f = []
    for (dirpath, dirnames, filenames) in walk(dirName):
        f.append(filenames)
    return f


def create_input_param(f,dir):
    """
    :param: fileNames as input to this function
    :return: returning list of words in each of the files
    """
    wordList = []
    for fileNames in f:
        for files in fileNames:
           fileName = dir + "/" + files
           f = open(fileName)
           lines = f.readlines()
           for words in lines:
                wordList.append(words)
           f.close()
    return wordList

def createFileWordMappings(dir):
    f = []
    f = get_fileNames(dir)
    maps = Maps()
    index = 0
    for file in f:
        for fileNames in file:
            maps.file_map[index] = fileNames
            index += 1
    print("File Mapping : ")
    print(maps.file_map)

    token_tuple_list = create_token_tuples(create_input_param(f,dir))
    maps.word_map = create_posting_lists(token_tuple_list)
    print("Word Mapping  : ")
    print(maps.word_map)
    return maps

def get_files(word,maps):
    files = []
    try:
        print("Word : " + word + " is present in following files")
        for file_index in maps.word_map[word]:
            try:
                files.append(maps.file_map[file_index])
            except:
                files = [maps.file_map[file_index]]
    except:
        print("Word not present in any of the files")

    return files


