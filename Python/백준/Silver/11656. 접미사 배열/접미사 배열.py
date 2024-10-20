S = input()

result = []
for i in range(len(S)):
    result.append(S[i:])

result.sort()

for w in result:
    print(w)