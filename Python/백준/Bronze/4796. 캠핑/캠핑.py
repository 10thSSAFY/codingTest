tc = 0
while True:
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break
    tc += 1
    result = (V // P) * L + min(L, (V % P))
    print(f'Case {tc}: {result}')