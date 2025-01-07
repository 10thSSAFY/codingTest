import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(5)
        continue
    print(4 * pow(5, n - 1, 1000000007) % 1000000007)