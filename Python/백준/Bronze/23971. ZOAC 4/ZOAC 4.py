import math

H, W, N, M = list(map(int,input().split(' ')))
a = math.ceil(H / (N + 1))
b = math.ceil(W / (M + 1))

print(a * b)