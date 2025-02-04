N, M, K = map(int, input().split())

arr = [[[] for _ in range(N)] for _ in range(N)]
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
fire = []
for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    fire.append(((ri - 1), (ci - 1), mi, si, di))

for _ in range(K):
    while fire:
        fr, fc, fm, fs, fd = fire.pop()
        nr = (fr + dr[fd] * fs) % N
        nc = (fc + dc[fd] * fs) % N
        arr[nr][nc].append((fm, fs, fd))

    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) >= 2:
                nm, ns, odd, even = 0, 0, 0, 0
                num = len(arr[r][c])
                while arr[r][c]:
                    fire_info = arr[r][c].pop()
                    nm += fire_info[0]
                    ns += fire_info[1]
                    if fire_info[2] % 2 == 1:
                        odd += 1
                    else:
                        even += 1
                nm, ns = nm // 5, ns // num
                if nm:
                    if odd == num or even == num:
                        for nd in range(0, 7, 2):
                            fire.append((r, c, nm, ns, nd))
                    else:
                        for nd in range(1, 8, 2):
                            fire.append((r, c, nm, ns, nd))
            elif arr[r][c]:
                fire_info = arr[r][c].pop()
                fire.append((r, c, fire_info[0], fire_info[1], fire_info[2]))

result = 0
for fire_info in fire:
    result += fire_info[2]

print(result)
