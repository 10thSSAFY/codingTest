N = int(input())
cnt = 0

while(N > 1):
    cnt += N // 5
    N //= 5

print(cnt)