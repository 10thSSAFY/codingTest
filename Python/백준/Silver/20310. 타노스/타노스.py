S = list(input().rstrip())
n = S.count('0')
m = S.count('1')

check = 0
for num in S:
    if check == m // 2:
        break
    if num == '1':
        S.remove(num)
        check += 1

check = 0
S = S[::-1]
for num in S:
    if check == n // 2:
        break
    if num == '0':
        S.remove(num)
        check += 1

for num in S[::-1]:
    print(num, end='')
