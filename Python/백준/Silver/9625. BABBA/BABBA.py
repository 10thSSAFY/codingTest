K = int(input())
dp = [(1, 0)]
for _ in range(K):
    a = dp[-1][0]
    b = dp[-1][1]
    dp.append((b, b + a))

print(dp[-1][0], dp[-1][1])