dic = {'Dhaka' : 1, 'Rajshahi' : 3, 'Comlilla' : 2}
print(dic['Dhaka'])

print(type(dic))

dic['Dhaka'] = 'First'
print(dic['Dhaka'])

del dic['Rajshahi']
print(dic)

dic ['Rajshahi'] = 3
print(dic)

for item in dic:
    print(item)


for item in dic:
    print(item, dic[item])


print(dic.keys())
dic.popitem()
print(dic)
dic ['Rajshahi'] = 3
print(dic)