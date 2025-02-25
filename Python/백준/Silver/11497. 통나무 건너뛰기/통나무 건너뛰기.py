T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    lst_1 = []
    lst_2 = []
    for i in range(len(lst)):
        if i % 2 == 0:
            lst_1.append(lst[i])
        else:
            lst_2.append(lst[i])

    l3 = lst_1 + lst_2[::-1]

    result = abs(l3[0] - l3[-1])
    for j in range(N - 1):
        if abs(l3[j] - l3[j + 1]) > result:
            result = abs(l3[j] - l3[j + 1])

    print(result)
