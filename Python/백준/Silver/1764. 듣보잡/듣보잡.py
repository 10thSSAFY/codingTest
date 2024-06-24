N, M = map(int, input().split())

set1 = set()
for _ in range(N):
    set1.add(input())

set2 = set()
for _ in range(M):
    set2.add(input())

result = sorted(list(set1 & set2))

print(len(result))
for r in result:
    print(r)
