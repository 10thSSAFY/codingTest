input = __import__('sys').stdin.readline

T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())

    r1 = a ** 2 + (b + c) ** 2
    r2 = b ** 2 + (a + c) ** 2
    r3 = c ** 2 + (a + b) ** 2
    print(min(r1, r2, r3))