import sys
input = sys.stdin.readline

def res4():
    return lst[N - 1] - lst[0]


def res3():
    D = dict()
    for i in range(N):
        if lst[i] in D:
            D[lst[i]] += 1
        else:
            D[lst[i]] = 1

    max_num = max(D.values())
    D_lst = []
    for i in D:
        if max_num == D[i]:
            D_lst.append(i)

    if len(D_lst) > 1:
        return D_lst[1]
    else:
        return D_lst[0]


def res2():
    return lst[(N - 1) // 2]


def res1():
    return round(sum(lst) / N)


N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(input())
lst.sort()

print(res1())
print(res2())
print(res3())
print(res4())