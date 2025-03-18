input = __import__('sys').stdin.readline

R, C, W, S = map(int, input().split())
r1 = (R + C) * W

if (R + C) % 2 == 0:
    r2 = max(R, C) * S
else:
    r2 = (max(R, C) - 1) * S + W

r3 = min(R, C) * S + abs(R - C) * W

print(min(r1, r2, r3))
