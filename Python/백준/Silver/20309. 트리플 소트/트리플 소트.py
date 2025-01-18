def solution():
    global result
    for i in range(N):
        if lst[i] % 2 == i % 2:
            result = 'NO'
            return


N = int(input())
lst = list(map(int, input().split()))

result = 'YES'
solution()
print(result)