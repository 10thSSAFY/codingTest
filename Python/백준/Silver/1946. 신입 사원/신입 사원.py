import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort()

    result = 1
    top = lst[0][1]

    for i in range(1, N):
        if top > lst[i][1]:
            result += 1
            top = lst[i][1]

    print(result)