N = int(input())
M = input()
K = int(input())

num = int(M, 2)

if num % 2 ** K == 0:
    print('YES')
else:
    print('NO')
