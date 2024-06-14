N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

for i in range(N):
    a, b, cnt = A[i], B[i], 0
    if a == b:
        result.append(0)
        continue
    if a > b and P > Q or a < b and P < Q:
        print('NO')
        exit()
    elif a > b:
        while a > b:
            a += P
            b += Q
            cnt += 1
            if cnt >= 10000:
                break
        if a == b:
            result.append(cnt)
        else:
            print('NO')
            exit()
    elif a < b:
        while a < b:
            a += P
            b += Q
            cnt += 1
            if cnt >= 10000:
                break
        if a == b:
            result.append(cnt)
        else:
            print('No')
            exit()

print('YES')
print(*result)
