n = 1000000
a = [False, False] + [True]*(n-1) # 0과 1은 제외
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())
for i in range(N):
    b = True
    S = int(input())
    for j in primes:
        if S % j == 0:
            b = False
    if b == True:
        print("YES")
    else:
        print("NO")