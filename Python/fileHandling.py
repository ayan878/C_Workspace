# Open a file in read mode
file = open("Python/example.txt", 'w')
file.write("Hi I'm Ayan Raza.I'm creating file.")

# Open a file in append mode
file = open("example.txt", "a")
file.write("i'm appending the text")

# file.app end("ayan")

# Open a file in write mode
file = open("example.txt", 'r')
data= file.read()
print(data)