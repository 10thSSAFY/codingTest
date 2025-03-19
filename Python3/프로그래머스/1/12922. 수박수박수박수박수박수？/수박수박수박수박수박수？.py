def solution(n):
    word = ['수', '박']
    answer = ''.join(word[i % 2] for i in range(n))
    return answer