#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg: %r, arg2: %r" % (arg1, arg2))

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg: %r, arg2: %r" % (arg1, arg2))

#this just takes one argument
def print_one(arg1):
    print("arg1: %r" %arg1)

def print_none():
    print("This is none!")

print_two("Tohid", "Fahim")
print_two_again("Tohid", "Tohid")
print_one("First!")
print_none()

