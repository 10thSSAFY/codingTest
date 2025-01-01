S = input()
result = 0
for i in range(len(S)):
    if S[i] in ['a', 'e', 'i', 'o', 'u']:
        result += 1

print(result)