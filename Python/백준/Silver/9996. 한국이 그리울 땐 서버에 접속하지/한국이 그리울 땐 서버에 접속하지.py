input = __import__('sys').stdin.readline

N = int(input())
P = input().rstrip().split("*")
length = len(P[0]) + len(P[1])

for _ in range(N):
    word = input().rstrip()
    if length > len(word):
        print('NE')
    else:
        if word[:len(P[0])] == P[0] and word[-len(P[1]):] == P[1]:
            print('DA')
        else:
            print("NE")
