N = int(input())

for i in range(1, N + 1):
    print("*" * i + " " * 2 * (N - i) + "*" * i)
for j in range(1, N):
    print("*" * (N - j) + " " * 2 * j + "*" * (N - j))