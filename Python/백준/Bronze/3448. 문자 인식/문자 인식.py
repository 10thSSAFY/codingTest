N = int(input())
for _ in range(N):
    A, R = 0, 0
    while True:
        try:
            S = input()
        except:
            break

        if S == '':
            break
        A += len(S)
        R += S.count('#')
    R = A - R
    res = float(round(R / A * 100, 1))
    if str(res).split('.')[-1] == '0':
        res = int(res)
    print(f'Efficiency ratio is {res}%.')