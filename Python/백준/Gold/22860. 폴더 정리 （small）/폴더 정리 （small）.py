input = __import__('sys').stdin.readline

def solution(start):
    global num
    stack = [start]
    while stack:
        curr_path = stack.pop()
        for i in D.get(curr_path):
            if i in D:
                stack.append(i)
            if i not in D:
                S.add(i)
                num += 1
    return


N, M = map(int, input().split())

D = dict()
for _ in range(N + M):
    P, F, C = input().rstrip().split()
    if P not in D:
        D[P] = []
    if C == '1' and F not in D:
        D[F] = []
    D[P].append(F)

Q = int(input())
for _ in range(Q):
    visit = []
    S = set()
    num = 0
    path = list(input().rstrip().split('/'))
    solution(path[-1])
    print(len(S), num)