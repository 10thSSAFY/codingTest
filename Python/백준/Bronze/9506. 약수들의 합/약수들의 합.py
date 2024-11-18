while True:
    N = int(input())
    if N == -1:
        break
    lst = []
    for i in range(1, N):
        if N % i == 0:
            lst.append(i)
    if sum(lst) == N:
        print(N, "=", end=" ")
        print(*lst, sep=" + ")
    else:
        print(N, "is NOT perfect.")