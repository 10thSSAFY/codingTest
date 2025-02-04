def solution(ec):
    c = ec
    for r in range(99, -1, -1):
        if 0 <= c - 1 and arr[r][c - 1]:
            while 0 <= c - 1 and arr[r][c - 1]:
                c -= 1
            continue
        elif c + 1 < 100 and arr[r][c + 1]:
            while c + 1 < 100 and arr[r][c + 1]:
                c += 1
            continue
    return c


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ec = arr[99].index(2)
    result = solution(ec)
    print(f'#{tc} {result}')
