T = int(input())
for _ in range(T):
    S, C = input().split()
    result = S.replace(C, '*')
    print(len(result))
