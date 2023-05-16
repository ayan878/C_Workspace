import os
file = open("Create.txt", 'w')
file.write("I'm creating file")
file.close()

file=open("Create.txt",'r')
data=file.read()
print(data)
file.close()
os.remove("Create.txt")
