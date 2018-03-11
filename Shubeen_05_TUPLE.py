tpl = (1, 2, 3, [3, 6, 1], 'string', 7.21)

print(tpl[0])
print(tpl[-1])

#this is "not mutable" like string, unlike list

t = (1, 2, 3)
a, b, c = t
print(b)

x = 5
y = 8
t = (x, y)
print(t)

lisst = list(tpl)
print(lisst)

tupl = 1, 2, 3
print(type(tupl))

#dangerous
t1 = 1
print(type(t1))

t2 = (1, )
print(type(t2))

for item in tpl:
    print(item)