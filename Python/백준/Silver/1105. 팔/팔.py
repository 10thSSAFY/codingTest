L, R = input().split()

result = 0
if len(L) != len(R):
    print(result)
else:
    for i in range(len(L)):
        if L[i] != R[i]:
            break
        if L[i] == '8':
            result += 1
    print(result)
