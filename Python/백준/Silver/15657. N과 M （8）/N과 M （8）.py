N, M = 0, 0
lst = []
tmp = []


def dfs(start, depth):
    global N, lst, tmp
    if depth == M:
        print(*tmp)
        return

    for i in range(start, N):
        tmp.append(lst[i])
        dfs(i, depth + 1)
        tmp.pop()


def main():
    global N, M, lst
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    dfs(0, 0)


if __name__ == '__main__':
    main()