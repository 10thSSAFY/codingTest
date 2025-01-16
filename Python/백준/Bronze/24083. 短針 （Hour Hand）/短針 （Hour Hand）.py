A = int(input())
B = int(input())
result = (A + B) % 12
if result == 0:
    print(12)
else:
    print(result)