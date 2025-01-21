N=int(input())
a,b,r=1,1,1
for _ in range(N-2):a,b,r=b,r,b+r
print(r)