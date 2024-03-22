def solution(n, computers):
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            
            while stack:
                num = stack.pop()
                for j in range(n):
                    if computers[num][j] == 1 and not visited[j]:
                        stack.append(j)
                        visited[j] = True
            answer += 1    
                
    return answer