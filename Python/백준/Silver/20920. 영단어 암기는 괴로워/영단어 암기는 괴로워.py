import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    words = {}
    for _ in range(N):
        word = input().rstrip()
        if len(word) < M:
            continue

        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    word_list = list(words.keys())
    word_list.sort()
    word_list.sort(key=len, reverse=True)
    word_list.sort(key=lambda x: words[x], reverse=True)

    print('\n'.join(word_list))

main()
