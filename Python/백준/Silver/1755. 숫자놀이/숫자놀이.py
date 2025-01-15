M, N = map(int, input().split())
ord = [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]

cnt = 0
result = ''
for i in range(10):
    if M <= ord[i] <= N:
        result += str(ord[i]) + ' '
        cnt += 1
        if not cnt % 10:
            result += '\n'

    if (M - 10 <= ord[i] * 10):
        for k in range(10):
            num = ord[i] * 10 + ord[k]
            if num < 10 or not(M <= num <= N):
                continue
            result += str(num) + ' '

            cnt += 1
            if not cnt % 10:
                result += '\n'

print(result)