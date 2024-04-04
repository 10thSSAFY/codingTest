K = int(input())
for i in range(1, K+1):
    print(f'Data Set {i}:')
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    code = list(input().strip())
    for line in lst:
        l = line.upper()
        for c in code:
            if c.upper() in l:
                l = l[l.index(c.upper())+1:]
            else:
                break
        else:
            print(line)

