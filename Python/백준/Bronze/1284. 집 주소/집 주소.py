input = __import__('sys').stdin.readline

while True:
    N = input().rstrip()
    if N == '0':
        break

    result = len(N) + 1
    for n in N:
        if n == '1':
            result += 2
        elif n == '0':
            result += 4
        else:
            result += 3

    print(result)
