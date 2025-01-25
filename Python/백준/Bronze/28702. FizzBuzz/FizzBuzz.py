A = input()
B = input()
C = input()

if A != 'FizzBuzz' and A != 'Fizz' and A != 'Buzz':
    result = int(A) + 3
elif B != 'FizzBuzz' and B != 'Fizz' and B != 'Buzz':
    result = int(B) + 2
else:
    result = int(C) + 1

if result % 15 == 0:
    result = 'FizzBuzz'
elif result % 3 == 0:
    result = 'Fizz'
elif result % 5 == 0:
    result = 'Buzz'

print(result)
