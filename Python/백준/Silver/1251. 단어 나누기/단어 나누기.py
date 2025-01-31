lst = list(input())
results = []
for i in range(1, len(lst) - 1):
    for j in range(i + 1, len(lst)):
        result = list(reversed(lst[:i])) + list(reversed(lst[i:j])) + list(reversed(lst[j:]))
        results.append(''.join(result))
results.sort()

print(results[0])
