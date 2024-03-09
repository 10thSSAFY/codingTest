N = int(input())
Nlst = set(list(map(int, input().split())))
M = int(input())
Mlst = list(map(int, input().split()))

for num in Mlst:
    if num in Nlst:
        print(1, end=' ')
    else:
        print(0, end=' ')
