i = 0
numbers = []

while i<6:
    print("At the top i is %d" %i)
    numbers.append(i)

    i = i+1
    print("Numbers Now : ", numbers)
    print("At the bottom i is %d" %i)

print("The Numbers : ")
for num in numbers:
    print(num)