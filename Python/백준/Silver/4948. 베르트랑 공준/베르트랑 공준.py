import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    s, e = N, N * 2
    prime = [1] * (e + 1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2, e + 1):
        if prime[i]:
            num = i * 2
            while num <= e:
                prime[num] = 0
                num += i
    print(sum(prime[s + 1 : e + 1]))
