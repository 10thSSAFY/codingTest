import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    if '0' in s:
        (f, e) = s.split('0')
        f = len(f)
        if e and f % 2 == 0:
            print(1)
        elif e and f % 2 == 1:
            print(0)
        elif not e and f % 2 == 0:
            print(0)
        elif not e and f % 2 == 1:
            print(1)
    else:
        (f, e) = s.split('1')
        f = len(f)
        if f % 2 == 0:
            print(1)
        else:
            print(0)
