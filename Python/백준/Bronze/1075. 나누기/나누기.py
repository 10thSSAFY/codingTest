N = input()
F = int(input())

N = int(N[:-2] + '00')
while True:
    if N % F == 0:
        break
    N += 1
print(str(N)[-2:])
