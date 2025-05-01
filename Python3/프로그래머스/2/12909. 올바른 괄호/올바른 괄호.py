def solution(s):
    S = []
    for t in s:
        if t == '(':
            S.append(1)
        else:
            if S:
                S.pop()
            else:
                return False
    if S:
        return False
    
    return True