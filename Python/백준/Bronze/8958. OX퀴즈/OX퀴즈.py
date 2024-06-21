T = int(input())
for _ in range(T):
    line = input()
    score = 0
    result = 0
    for i in range(len(line)):
        if line[i] == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)
