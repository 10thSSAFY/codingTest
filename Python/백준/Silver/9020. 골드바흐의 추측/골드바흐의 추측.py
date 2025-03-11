import sys
input = sys.stdin.readline

prime = [True] * 10001
prime[0] = False
prime[1] = False

for i in range(2, 10001):
    if prime[i]:
        n = i * i
        while n <= 10000:
            if prime[n]:
                prime[n] = False
            n += i

T = int(input())
for _ in range(T):
    N = int(input())
    a = b = 0
    min_diff = 1e8
    for i in range(2, N // 2 + 1):
        if prime[i] and prime[N - i] and min_diff > N - i - i:
            min_diff = N - i - i
            a, b = i, N - i
    print(a, b)
