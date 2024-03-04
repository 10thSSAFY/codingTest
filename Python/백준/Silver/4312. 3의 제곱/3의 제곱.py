import sys
input = sys.stdin.readline

while True:
    N = int(input())
    lst = []
    if N == 0:
        break
        
    N -= 1
    while N != 0:
        lst.append(N % 2)
        N = N >> 1
    
    num = 1
    ans = '{ '
    for i in lst:
        if i == 1:
            ans += str(num) + ', '
        num *= 3

    if len(ans) > 2:
        ans = ans[:-2]
        ans += " }"
        print(ans)
    else:
        print('{ }')
