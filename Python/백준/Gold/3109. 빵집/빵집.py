import sys
input = sys.stdin.readline

def dfs(r, c):
    if c == C - 1:
        return True
    for dr in [-1, 0, 1]:
        nr, nc = r + dr, c + 1
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if arr[nr][nc] != 'x' and not visited[nr][nc]:
            visited[nr][nc] = True
            if dfs(nr, nc):
                return True
    return False


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

result = 0
for i in range(R):
    if dfs(i, 0):
        result += 1

print(result)