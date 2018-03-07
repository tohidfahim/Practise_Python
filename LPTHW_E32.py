the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'prnnies', 2, 'dimes', 3, 'quarters']

#the first kinf of for-loop goes through a list
for number in the_count:
    print(number)

#same as above
for fruit in fruits:
    print(fruit)

for i in change:
    print(i)

#we can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i) #add

for i in elements:
    print("Element was: %d" % i)