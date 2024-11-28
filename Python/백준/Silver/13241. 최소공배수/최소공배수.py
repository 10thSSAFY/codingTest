def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

a, b = map(int, input().split())
print(a * b // gcd(a, b))