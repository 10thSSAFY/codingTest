def change(r, nr, c, nc, n):
    for i in range(r, nr + 1):
        for j in range(c, nc + 1):
            arr[i][j] = n


def is_condition(r, nr, c, nc):
    for i in range(r, nr + 1):
        for j in range(c, nc + 1):
            if not arr[i][j]:
                return False
    return True


def solution(cnt):
    global result
    for r in range(10):
        for c in range(10):
            if arr[r][c]:
                for size in range(5):
                    if paper[size] and r + size < 10 and c + size < 10:
                        nr, nc = r + size, c + size
                        if is_condition(r, nr, c, nc):
                            change(r, nr, c, nc, 0)
                            paper[size] -= 1
                            solution(cnt + 1)
                            paper[size] += 1
                            change(r, nr, c, nc, 1)
                return
    result = min(result, cnt)


arr = [list(map(int, input().split())) for _ in range(10)]
paper = [5, 5, 5, 5, 5]
result = 26
solution(0)
print(result if result != 26 else -1)
