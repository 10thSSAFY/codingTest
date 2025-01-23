N = int(input())
S1 = input()
S2 = input()

ords = [0] * 26
for i in range(N):
    ords[ord(S1[i]) - ord('a')] += 1

result = 0
for j in range(N):
    if ords[ord(S2[j]) - ord('a')]:
        ords[ord(S2[j]) - ord('a')] -= 1
    else:
        result += 1

print(result)