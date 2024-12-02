num = 0
for _ in range(10):
    n = int(input())
    if abs(100 - (num + n)) <= abs(100 - num):
        num += n
    else:
        break
        
print(num)
