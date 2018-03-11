a = set()
print(a)

b = set('abcd')
print(b)

#ERROR
# a = set(1, 2, 3, 4)
# a = set(1)

#we can make set from list and tuple
tpl = (1, 3, 9, 9, 4, 1)
lt = [5, 1, 3, 5]

s1 = set(tpl)
print(s1)

s2 = set(lt)
print(s2)

#operation
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

print(7 in s1)