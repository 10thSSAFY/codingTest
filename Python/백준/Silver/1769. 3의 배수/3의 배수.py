S = input()

result = 0
while len(S) > 1:
    result += 1
    tmp= 0
    for i in range(len(S)):
        tmp += int(S[i])
    S = str(tmp)
    
print(result)
if int(S) % 3 == 0:
    print('YES')
else:
    print('NO')