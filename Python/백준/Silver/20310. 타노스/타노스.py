S = list(input().rstrip())
n = len(S) // 2
m = S.count('1') // 2
result = '0' * (n - m) + '1' * m
print(result)