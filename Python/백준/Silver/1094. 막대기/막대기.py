N = int(input())

length = 64
cnt = 0
while N != length:
    if N > length:
        N -= length
        cnt += 1
    length //= 2

print(cnt + 1)