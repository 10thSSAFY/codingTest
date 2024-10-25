N = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = 1

for num in lst:
    if result < num:
        break
    result += num

print(result)