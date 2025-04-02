input = __import__('sys').stdin.readline

N = int(input())
S = set()
cnt = 0
for _ in range(N):
    I = input().rstrip()
    if I == 'ENTER':
        S.clear()
    else:
        if I not in S:
            cnt += 1
        S.add(I)

print(cnt)
