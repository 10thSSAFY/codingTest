T = int(input())
An = int(input())
A = list(map(int, input().split()))
Bn = int(input())
B = list(map(int, input().split()))

sumA = [0] * (An + 1)
for i in range(An):
    sumA[i+1] = sumA[i] + A[i]

sumB = [0] * (Bn + 1)
for i in range(Bn):
    sumB[i+1] = sumB[i] + B[i]

dictA = {}
for e in range(1, An + 1):
    for s in range(e):
        prefix = sumA[e] - sumA[s]
        if prefix in dictA:
            dictA[prefix] += 1
        else:
            dictA[prefix] = 1

dictB = {}
for e in range(1, Bn + 1):
    for s in range(e):
        prefix = sumB[e] - sumB[s]
        if prefix in dictB:
            dictB[prefix] += 1
        else:
            dictB[prefix] = 1

result = 0
for preNum, cnt in dictA.items():
    if T - preNum in dictB:
        result += dictA[preNum] * dictB[T - preNum]

print(result)