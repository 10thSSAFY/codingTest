S = list(input().strip())
T = list(input().strip())

lst = [0] * len(T)
for s in S:
    if s in T:
        if T.index(s) == 0 or lst[T.index(s) - 1] > lst[T.index(s)]:
            lst[T.index(s)] += 1

print(lst[-1])
