N, M, K = map(int, input().split())

while K < 0:
    K += N

result = (((K - 3) % N) + M)
if result > N:
    result %= N
    
print(result)