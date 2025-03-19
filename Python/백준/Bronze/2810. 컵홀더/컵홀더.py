input = __import__('sys').stdin.readline

N = int(input())
member = input().rstrip()

count = member.count('LL')

if count <= 1:
    print(len(member))
else:
    print(len(member) - count + 1)
