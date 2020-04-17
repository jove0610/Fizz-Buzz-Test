print('Enter any key to begin')
input()
for i in range(100):
    i = i + 1
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(str(i))
print('Enter any key to exit')
input()
