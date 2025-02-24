name = input()

lst = []
cnt = dict()
for n in name:
    if n in cnt:
        cnt[n] += 1
    else:
        lst.append(n)
        cnt[n] = 1

odd = []
for key, value in cnt.items():
    if value % 2 == 1:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    result = ''
    
    lst.sort()
    for w in lst:
        result += w * (cnt[w] // 2)
        
    if odd:
        result += odd.pop() + result[::-1]
    else:
        result += result[::-1]
        
    print(result)
