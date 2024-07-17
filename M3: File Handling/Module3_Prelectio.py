# FILE HANDLING
# - open function (opening a file)
# - there are 4 different methods

# myfile = open ("filename", "mode")

# + indicated both read and write.
# you can not use + if you just want to write or read

# Writing on file (creating a file if not yet existing)
    # - if there is an existing file, it will overwritten the text in file
myfile = open ("d:\filehandling.txt", "w+")
# myfile.write("Hello in line 1")
# myfile.close()

# overwriting an existing file
# myfile.write("OOPS NEW CONTENT")

# Appending data to a text file. (file is already existing)
myfile = open ("d:\filehandling", "a+")
# myfile.write("New file")
# myfile.close()
# myfile = open("d:\filehandling", "r") # to check the append
# print(myfile.read())

# Reading text file. (file is already existing)
myfile = open ("d:\filehandling","r") # no + sign
# print(myfile.read()) # will print the whole text

# print(myfile.read(5)) # char; first 5 char

# print(myfile.readline()) # return 1 line 

# print(myfile.readline())

# for x in myfile:
#       print (x)   # printing all line but with created space

# Creating a file (no file existing; error if it is existing)
myfile = open ("d:\NEWfilehandling.txt", "x")

# Additional modes:
myfile = open (":d\filehandling.txt", "t")
myfile = open (":d\filehandling.txt", "b") # writing binary

# Removing / Deleting the text file
# you need an OS module because operating system is responsible for deleting a file (not python !)
import os  #OS module
if os.path.exists("d:/filehandling.txt"):
    os.remove("d:/filehandling.txt")
    print("File has been deleted")
else:
    print("File does not exists")

