import sys
input = sys.stdin.readline

prime = [True] * 1000001
for i in range(2, int(1000001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False


while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if prime[i] and prime[n - i]:
            print(f'{n} = {n - i} + {i}')
            break
