def gcd(a, b):
    while b > 0:
        a, b = b, a % b,
    return a


A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

newA, newB = A1 * B2 + A2 * B1, B1 * B2

d = gcd(newA, newB)
newA //= d
newB //= d

print(newA, newB)