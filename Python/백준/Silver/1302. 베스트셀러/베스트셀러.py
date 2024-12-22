N = int(input())

dic = dict()
for _ in range(N):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

lst = []
cnt = max(dic.values())
for key, value in dic.items():
    if value == cnt:
        lst.append(key)

lst.sort()
print(lst[0])