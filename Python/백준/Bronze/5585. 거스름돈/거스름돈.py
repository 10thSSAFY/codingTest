N = int(input())
m = 1000 - N

money = [500, 100, 50, 10, 5, 1]
count = 0
for i in money:
    count += m // i
    m %= i

print(count)