print ("Hello World")

num1 = 30
print (type(num1))

num2 = 5.5
print(type(num2))

num3 = num1 + num2
print(num3)
print(type(num3))

#String Here
str = "Bangladesh"
print (type(str))

str2 = "Ansar\'s"
print(str2)

print(str2[2])
print(len(str2))

country = "Bangla" + "Desh"
print(country)
print(country.find('D'))
print(country.__len__())

new_country = country.replace('D', 'd')
print(new_country)
print(country)

stri = "  a   sad sa r    g"
stri2 = stri.strip()
print(stri2)

print(country.upper())

#swap is easy
a = 10
b = 20
print(a, b)
(a, b) = (b, a)
print(a, b)
