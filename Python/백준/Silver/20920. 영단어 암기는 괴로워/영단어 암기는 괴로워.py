import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    words = dict()

    for _ in range(N):
        word = input().strip()
        if len(word) < M:
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    word_list = sorted(words.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

    for w in word_list:
        print(w[0])

main()