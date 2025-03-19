def solution(n):
    word = ['수', '박']
    answer = ''
    for i in range(n):
        answer += word[i % 2]
    return answer