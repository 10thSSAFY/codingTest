N = int(input())
lst = list(map(int, input().split()))

s_lst = sorted(list(set(lst)))
dic = {s_lst[i] : i for i in range(len(s_lst))}

for l in lst:
    print(dic[l], end=' ')