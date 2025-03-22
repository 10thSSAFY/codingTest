from math import *
D, H, W=  map(int, input().split())

x = pow(D, 2) / (pow(H, 2) + pow(W, 2))
x = sqrt(x)

height = H * x
weight = W * x
print(floor(height), floor(weight))