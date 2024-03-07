import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 1001

for i in range(N):
    a, b = input().split()
    lst[int(b)] += 1
    if a == "jinju":
        m = int(b)

print(m)
print(sum(lst[m+1:]))