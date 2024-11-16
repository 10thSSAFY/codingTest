S = input()
idx = 0
result = ''
for _ in range(len(S)):
    result += S[idx]
    idx += 1
    if idx % 10 == 0:
        print(result)
        result = ''
        
print(result)