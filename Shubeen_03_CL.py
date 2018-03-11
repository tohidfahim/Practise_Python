vowels = ['a', 'e', 'i', 'o', 'u']

x = 'i'

if x in vowels:
    print('vowel')
else:
    print('consonent')

for i in vowels:
    print(i)

print(range(10))
print(list(range(5, 10)))
print("Fibonacci")
fib_1 = 0
fib_2 = 1

print(fib_1)
print(fib_2)

while fib_2 < 20 :
    fib = fib_1 + fib_2
    print(fib)
    (fib_1, fib_2) = (fib_2, fib)
