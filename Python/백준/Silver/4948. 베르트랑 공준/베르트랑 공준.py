import sys
input = sys.stdin.readline


prime = [1] * 246913
prime[0] = 0
prime[1] = 0
for i in range(2, 246913):
    if prime[i]:
        num = i * 2
        while num <= 246912:
            prime[num] = 0
            num += i

while True:
    N = int(input())
    if N == 0:
        break
    print(sum(prime[N + 1 : N * 2 + 1]))
