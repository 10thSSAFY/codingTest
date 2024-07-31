S = input()
q = int(input())

arr = [[0] * 26 for _ in range(len(S) + 1)]
for i in range(len(S)):
    for j in range(26):
        arr[i+1][j] = arr[i][j]
    arr[i+1][ord(S[i]) - 97] += 1

for _ in range(q):
    a, l, r = input().split()
    idx = ord(a) - 97
    print(arr[int(r) + 1][idx] - arr[int(l)][idx])
