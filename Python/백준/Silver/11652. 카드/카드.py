input = __import__('sys').stdin.readline

N = int(input())

D = dict()
for _ in range(N):
    num = int(input())
    if num in D:
        D[num] += 1
    else:
        D[num] = 1

result = sorted(D.items(), key=lambda x:(-x[1], x[0]))
print(result[0][0])