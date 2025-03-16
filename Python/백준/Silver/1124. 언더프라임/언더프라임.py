import math
input = __import__('sys').stdin.readline


def solution(n):
    cnt = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            cnt += 1
            n //= i
    if n != 1:
        cnt += 1
    return cnt


A, B = map(int, input().split())
prime = [True for i in range(B + 1)]

prime[1] = False
for i in range(2, B + 1):
    if not prime[i]:
        continue

    for j in range(i * i, B + 1, i):
        prime[j] = False

result = 0
for i in range(A, B + 1):
    if prime[solution(i)]:
        result += 1

print(result)
