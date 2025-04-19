input = __import__('sys').stdin.readline

N = int(input())

D = dict()
result = 0
for _ in range(N):
    cow, load = map(int, input().split())
    if cow in D:
        if D[cow] != load:
            D[cow] = load
            result += 1
    else:
        D[cow] = load

print(result)
