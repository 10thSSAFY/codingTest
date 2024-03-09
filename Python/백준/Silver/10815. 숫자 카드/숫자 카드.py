N = int(input())
Nlst = set(list(map(int, input().split())))
M = int(input())
Mlst = list(map(int, input().split()))

for num in Mlst:
    print(1 if num in Nlst else 0, end=' ')
