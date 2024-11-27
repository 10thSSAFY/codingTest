import sys
input = sys.stdin.readline


N = int(input())
lst = []
for _ in range(N):
    name, korean, english, math = input().split()
    lst.append((-int(korean), int(english), -int(math), name))
lst.sort()

for i in range(N):
    print(lst[i][3])