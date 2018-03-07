from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying files from %s to %s" %(from_file, to_file))

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" %len(indata))

print("Does the output file exist? %r" % exists(to_file))

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done!")

out_file.close()
in_file.close()

#python LPTHW_E17.py LPTHW_E16.txt LPTHW_E17.txt