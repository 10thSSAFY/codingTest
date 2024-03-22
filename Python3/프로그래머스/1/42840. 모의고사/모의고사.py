def solution(answers):
    spj1 = [1, 2, 3, 4, 5]
    spj2 = [2, 1, 2, 3, 2, 4, 2, 5]
    spj3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = score2 = score3 = 0
    
    for i in range(len(answers)):
        if spj1[i % 5] == answers[i]:
            score1 += 1
        if spj2[i % 8] == answers[i]:
            score2 += 1
        if spj3[i % 10] == answers[i]:
            score3 += 1
            
    answer = []
    max_score = max(score1, score2, score3)
    if score1 == max_score:
        answer.append(1)
    if score2 == max_score:
        answer.append(2)
    if score3 == max_score:
        answer.append(3)
        
    return answer