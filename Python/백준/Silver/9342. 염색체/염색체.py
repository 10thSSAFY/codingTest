import re

t = int(input())
a = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(t):
    if a.match(input())==None:
        print('Good')
    else:
        print('Infected!')