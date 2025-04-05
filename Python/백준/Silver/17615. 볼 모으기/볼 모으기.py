N = int(input())
balls = input().rstrip()

R1 = balls.lstrip('R').count('R')
R2 = balls.rstrip('R').count('R')
B1 = balls.rstrip('B').count('B')
B2 = balls.rstrip('B').count('B')

print(min(R1, R2, B1, B2))
