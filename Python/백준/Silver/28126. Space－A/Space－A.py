import sys
input = sys.stdin.readline

N = int(input())
order = input().strip()

R, U, X = 0, 0, 0
for w in order:
    if w == 'R':
        R += 1
    elif w == 'U':
        U += 1
    else:
        X += 1

K = int(input())

result = 0
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    m = min(x, y, X)
    x -= m + R
    y -= m + U

    if x <= 0 and y <= 0:
        result += 1

print(result)
