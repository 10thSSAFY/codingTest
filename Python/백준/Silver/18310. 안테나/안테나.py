N = int(input())
lst = sorted(list(map(int, input().split())))

print(lst[(N - 1) // 2])