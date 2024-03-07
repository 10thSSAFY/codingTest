import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()
res = 0
for  _ in range(N//3):
    res += lst.pop()
    res += lst.pop()
    lst.pop()

print(res + sum(lst))