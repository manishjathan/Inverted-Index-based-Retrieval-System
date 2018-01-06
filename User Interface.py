from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import Interface




def openDirectory():
    dirName = askdirectory()
    entry1.insert(0,str(dirName))
    print(dirName)

def searchWord():
    maps = Interface.createFileWordMappings(entry1.get())
    word = entry2.get().lower()
    files = Interface.get_files(word, maps)
    for file in files:
        text.insert(END, file + "\n")


root =Tk()
root.title("Inverted Index DRS")
root.geometry("400x400")

topFrame = Frame(root)
topFrame.pack()

middleFrame = Frame(root)
middleFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)

label_3 = Label(middleFrame, text = "Enter the folder to search")
entry1 = Entry(middleFrame,width =100)
button1 = Button(middleFrame, text = "Browse Folder",command = openDirectory,width = 30)

label_1 = Label(topFrame, text ="Enter the word to search",width = 125)
button2 = Button(topFrame, text = "Search",command = searchWord,width=20)
entry2 = Entry(topFrame,width=100)

label_2 = Label(bottomFrame,text = "Word present in following files : ")
text = Text(bottomFrame,width = 100,height = 100)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)

entry2.pack(side = TOP)
button2.pack(side = TOP)

label_2.pack(side = TOP)
text.pack(side = TOP)

root.mainloop()