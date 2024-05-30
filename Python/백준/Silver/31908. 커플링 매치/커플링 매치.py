N = int(input())

couple = {}
for _ in range(N):
    name, ring = map(str, input().split())
    if ring not in couple and ring != '-':
        couple[ring] = [name]
    elif ring in couple:
        couple[ring].append(name)

cnt = 0
couples = []
for key, value in couple.items():
    if len(value) == 2:
        cnt += 1
        couples.append(value)

print(cnt)
for c in couples:
    print(*c)