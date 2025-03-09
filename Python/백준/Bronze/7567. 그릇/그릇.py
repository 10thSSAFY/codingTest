lst = list(str(input()))
result = 0

for i in range(len(lst)):
    if i == 0:
        result += 10
    elif lst[i] == lst[i - 1]:
        result += 5
    else:
        result += 10

print(result)