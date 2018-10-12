from tkinter import filedialog
from tkinter import *
root = Tk()#.withdraw()
#source_directory = filedialog.askdirectory()

root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)


file=open(root.filename)

wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();