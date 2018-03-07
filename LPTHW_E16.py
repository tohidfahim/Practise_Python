print("Type The File Name : ")
filename = input()

print("We are going to erase %r." %filename)

print("Opening the file....")
target = open(filename, 'w')

print("Trunncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print("And finally we close it.")
target.close()