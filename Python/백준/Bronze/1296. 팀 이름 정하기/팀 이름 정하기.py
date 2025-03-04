S = input()
N = int(input())

T = [0] * N
for i in range(N):
    T[i] = input().rstrip()
T.sort()

result = ""
max_num = -1
for i in range(N):
    word = S + T[i]
    L = word.count('L')
    O = word.count('O')
    V = word.count('V')
    E = word.count('E')
    total = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if total > max_num:
        result = T[i]
        max_num = total

print(result)
