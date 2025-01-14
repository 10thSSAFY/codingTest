def solution(g):
    if g == 1:
        return True

    for i in range(N):
        if abs(A[i] - i) % g != 0:
            return False

    return True


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N, K = map(int, input().split())
A = list(map(int, input().split()))
g = gcd(N, K)

if solution(g):
    print('YES')
else:
    print('NO')