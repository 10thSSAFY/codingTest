import sys
input = sys.stdin.readline


def move():
    tmp = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                nr, nc = r, c
                s, d, z = arr[r][c][0]
                speed = s
                if d == 0 or d == 1:
                    speed %= (R - 1) * 2
                else:
                    speed %= (C - 1) * 2

                while speed:
                    if d == 0: # 상
                        if speed >= nr:
                            speed -= nr
                            nr = 0
                            d = 1
                        else:
                            nr -= speed
                            speed = 0
                    elif d == 1: # 하
                        if speed >= R - nr - 1:
                            speed -= R - nr - 1
                            nr = R - 1
                            d = 0
                        else:
                            nr += speed
                            speed = 0
                    elif d == 2: # 우
                        if speed >= C - nc - 1:
                            speed -= C - nc - 1
                            nc = C - 1
                            d = 3
                        else:
                            nc += speed
                            speed = 0
                    elif d == 3: # 좌
                        if speed >= nc:
                            speed -= nc
                            nc = 0
                            d = 2
                        else:
                            nc -= speed
                            speed = 0

                tmp[nr][nc].append((s, d, z))

    for r in range(R):
        for c in range(C):
            if len(tmp[r][c]) >= 2:
                tmp[r][c].sort(key=lambda x: x[2], reverse=True)
                tmp[r][c] = [tmp[r][c][0]]

    return tmp


def catch(c):
    global result
    for r in range(R):
        if arr[r][c]:
            result += arr[r][c].pop()[2]
            return


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C, M = map(int, input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r - 1][c - 1].append((s, d - 1, z))

result = 0
for i in range(C):
    catch(i)
    arr = move()

print(result)