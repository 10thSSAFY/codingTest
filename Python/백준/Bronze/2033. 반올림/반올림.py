N = int(input())
curr = 10
result = N

while result > curr:
    if result % curr >= curr // 2:
        result += curr
    result -= (result % curr)
    curr *= 10

print(result)
