S = list(input().strip())
T = list(input().strip())

result = 0
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

    if S == T:
        result = 1
        break

print(result)