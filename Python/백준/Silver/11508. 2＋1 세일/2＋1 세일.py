from sys import stdin
input = stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()
res = sum(lst)
free = sum(lst[-3::-3])
print(res - free)