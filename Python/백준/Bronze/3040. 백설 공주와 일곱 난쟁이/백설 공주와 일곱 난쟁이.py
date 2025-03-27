lst = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i + 1, 9):
        if sum(lst) - lst[i] - lst[j] == 100:
            x, y = i, j
            break
            
lst.pop(x)
lst.pop(y - 1)
for i in lst:
    print(i)
