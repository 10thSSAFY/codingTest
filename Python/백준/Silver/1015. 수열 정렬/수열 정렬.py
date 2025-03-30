input = __import__('sys').stdin.readline

N = int(input())
A = list(map(int, input().split()))
newA = sorted(A)

P = []
for i in range(N):
    P.append(newA.index(A[i]))
    newA[newA.index(A[i])] = False

print(*P)