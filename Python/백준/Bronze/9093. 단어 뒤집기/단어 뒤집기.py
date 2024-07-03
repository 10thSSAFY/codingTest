n = int(input())

for i in range(n):
    s = list(input().split())
    for j in s:
        print(j[::-1], end=" ")
    print()
