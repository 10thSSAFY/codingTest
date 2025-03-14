S = input()

if S == S[::-1]:
    print(len(S))
else:
    n = 1
    while True:
        if S[n:] == S[len(S)-1:n-1:-1]:
            break
        n += 1
    print(len(S) + n)