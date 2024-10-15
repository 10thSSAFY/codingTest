N = int(input())

M_lst = []
for _ in range(N):
    lst = list(input().split())
    if lst[1] == 'jaehak' and lst[2] == 'notyet' and lst[3] not in '123':
        M_lst.append((int(lst[4]), lst[0]))

M_lst.sort()
M_lst = M_lst[:10]

result = []
for m in M_lst:
    result.append(m[1])

result.sort()

print(len(result))
for r in result:
    print(r)