N = int(input())

lst = []
for _ in range(N):
    S = input()
    num = 0
    flag = False
    for i in range(len(S)):
        if '0' <= S[i] <= '9':
            num = num * 10 + int(S[i])
            flag = True
        elif flag == True:
            lst.append(num)
            num = 0
            flag = False
    if flag:
        lst.append(num)

lst.sort()
for n in lst:
    print(n)