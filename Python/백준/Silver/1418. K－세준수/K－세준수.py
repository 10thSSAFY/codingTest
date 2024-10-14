N = int(input())
K = int(input())

p = [0 for i in range(N + 1)]
for i in range(2, N + 1):
    if p[i] == 0:
        for t in range(i, N + 1, i):
            if t % i == 0:
                p[t] = max(p[t], i)

result = 0
for j in p:
    if j <= K:
        result += 1

print(result - 1)