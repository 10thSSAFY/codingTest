from collections import deque

def solution(begin, target, words):
    N = len(words)
    M = len(begin)
    q = deque([begin])
    visited = [False] * N

    answer = 0
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            w = q.popleft()
            for i in range(N):
                if not visited[i]:
                    tmp = 0
                    for j in range(M):
                        if w[j] != words[i][j]:
                            tmp += 1
                    if tmp == 1:
                        q.append(words[i])
                        visited[i] = True
                        if words[i] == target:
                            return cnt

    return answer