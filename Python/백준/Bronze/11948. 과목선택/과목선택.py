P = int(input())
C = int(input())
L = int(input())
E = int(input())
H = int(input())
G = int(input())

result = P + C + L + E - min(P, C, L, E) + max(H, G)
print(result)
