input = __import__('sys').stdin.readline

N = int(input())
lst = [input().rstrip() for _ in range(N)]
lst.sort(key=len)

res = 0
for i in range(N):
    flag = False
    for j in range(i + 1, N):
        if lst[i] == lst[j][0:len(lst[i])]:
            flag = True
            break

    if not flag:
        res += 1

print(res)