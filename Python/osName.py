import os
print(os.name)
print(dir(os)) # complete directory of os(methods and attrributes)
print(os.getcwd()) # it return current working directory
print(os.mkdir("Python/newDir")) #it is used to create new directory
print(os.rmdir("Python/newDir")) #it is used to delete absolute directory
print(os.listdir("Python"))#os.listdir() to get the lsit of all files and directory in the specify directory if we dont specify directory then it show list of files of current working directory
