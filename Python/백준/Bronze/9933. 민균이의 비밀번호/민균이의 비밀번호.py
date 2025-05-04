N = int(input())
lst = [input() for _ in range(N)]

for word in lst:
    if word[::-1] in lst:
        print(len(word), word[len(word) // 2])
        break
