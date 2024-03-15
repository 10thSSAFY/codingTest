N = int(input())

arr = [input().strip() for _ in range(N)]
arr_T = [''.join(i) for i in zip(*arr)]

width = 0
length = 0

for i in range(N):
    for j in arr[i].split('X'):
        if '..' in j:
            width += 1

    for j in arr_T[i].split('X'):
        if '..' in j:
            length += 1

print(width, length)
