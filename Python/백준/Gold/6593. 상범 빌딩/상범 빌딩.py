from collections import deque


def solution(sl, sr, sc, el, er, ec):
    q = deque([(sl, sr, sc, {(sl, sr, sc)}, 0)])
    while q:
        l, r, c, S, cnt = q.popleft()
        for i in range(6):
            nl, nr, nc = l + dl[i], r + dr[i], c + dc[i]
            if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C):
                continue

            if (nl, nr, nc) == (el, er, ec):
                return 'Escaped in ' + str(cnt + 1) + ' minute(s).'

            if box[nl][nr][nc] == '.' and (nl, nr, nc) not in S:
                S.add((nl, nr, nc))
                q.append((nl, nr, nc, S, cnt + 1))

    return 'Trapped!'


dl = [-1, 0, 0, 0, 0, 1]
dr = [0, -1, 0, 1, 0, 0]
dc = [0, 0, 1, 0, -1, 0]

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break

    sl, sr, sc = -1, -1, -1
    el, er, ec = -1, -1, -1

    box = [[] for _ in range(L)]
    for l in range(L):
        for r in range(R):
            line = input()
            if 'S' in line:
                sl, sr, sc = l, r, line.index('S')
            if 'E' in line:
                el, er, ec = l, r, line.index('E')
            box[l].append(line)
        input()

    result = solution(sl, sr, sc, el, er, ec)
    print(result)
