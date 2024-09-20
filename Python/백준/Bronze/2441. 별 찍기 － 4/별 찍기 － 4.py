N = int(input())
for i in range(N):
    line = ''
    line += ' ' * i
    line += '*' * (N - i)
    print(line)