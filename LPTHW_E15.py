#from sys import argv

#script, filename = argv

#txt = open(filename)

#print("Here's your file %r: " %filename)
#print(txt.read())
# python LPTHW_E15.py LPTHW_E15.txt (command promt)

print("Type The File Name : ")
txt_again = input()

txt_again = open(txt_again)
print(txt_again.read())