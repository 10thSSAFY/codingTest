input = __import__('sys').stdin.readline

S1, S2, S3 = map(int, input().split())

cnt = [0 for i in range(S1 + S2 + S3 + 1)]

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            cnt[i + j + k] += 1

print(cnt.index(max(cnt)))
