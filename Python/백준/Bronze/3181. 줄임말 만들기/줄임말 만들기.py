S = list(input().split())
ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

result = ''
for i in range(len(S)):
    if i != 0 and S[i] in ignore:
        continue
    result += chr(ord(S[i][0]) - 32)

print(result)
