def check(r, c, size):
    global white, blue
    cnt = 0
    for i in range(r, r + size):
        for j in range(c, c + size):
            cnt += arr[i][j]
    if cnt == 0:
        white += 1
        return True
    elif cnt == size * size:
        blue += 1
        return True

    return False


def solution(r, c, size):
    if check(r, c, size):
        return

    solution(r, c, size // 2)
    solution(r + size // 2, c, size // 2)
    solution(r, c + size // 2, size // 2)
    solution(r + size // 2, c + size // 2, size // 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
solution(0, 0, N)

print(white)
print(blue)