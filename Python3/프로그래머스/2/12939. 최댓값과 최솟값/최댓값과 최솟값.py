def solution(s):
    lst = list(map(int, s.split()))
    min_num = min(lst)
    max_num = max(lst)
    answer = str(min_num) + ' ' + str(max_num)
    return answer