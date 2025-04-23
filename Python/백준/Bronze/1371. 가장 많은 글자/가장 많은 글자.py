lst = [0] * 26

while True:
    try:
        line = input().rstrip()
        N = len(line)
        for i in range(N):
            if line[i] == ' ':
                continue
            lst[ord(line[i]) - 97] += 1
    except:
        break

for j in range(26):
    if lst[j] == max(lst):
        print(chr(j + 97), end='')
