def solution(s):
    lst = s.split(' ')
    
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()
        
    return ' '.join(lst)