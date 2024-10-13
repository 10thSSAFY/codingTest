a = list(map(int, input().split()))
min_num = min(a)

while True:
    cnt = 0
    for i in a:
        if min_num % i == 0:
            cnt += 1
    if cnt > 2:
        break
    min_num += 1
    
print(min_num)