lisst = [1, 4, 6, 9, 3, 5]

print(lisst)

lisst.reverse()
print(lisst)

lisst.sort()
print(lisst)

lisst.append(9)
print(lisst)

lisst.insert(2, 69)
print(lisst)

lisst2 = [10, 21]
print(lisst2)

lisst.extend(lisst2)
print(lisst)

print(lisst.count(9))

lisst.remove(69)
print(lisst)

lisst.pop()
print(lisst)

lisst.pop(2)
print(lisst)

lisst2 = [0] * 50
print(lisst2)

lisst2 = lisst
print(lisst2)

lisst2[0] = 9
print(lisst)

#list comprehension

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [li for li in li if li%2 == 1]
print(odd)