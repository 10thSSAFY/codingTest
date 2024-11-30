T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[-3])