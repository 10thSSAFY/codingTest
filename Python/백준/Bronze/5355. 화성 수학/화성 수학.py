import math

T = int(input())
for _ in range(T):
    num, *lst = input().split()
    num = float(num)
    for a in lst:
        if a == '@':
            num *= 3
        elif a == '%':
            num += 5
        elif a == '#':
            num -= 7

    print("%.2f" % num)