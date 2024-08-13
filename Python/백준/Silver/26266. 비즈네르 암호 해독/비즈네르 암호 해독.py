P = input()
S = input()

Pn = len(P)

P_list = [0] * Pn
S_list = [0] * Pn
R_list = [0] * Pn

for i in range(Pn):
    R_list[i] = ord(S[i]) - 64 - (ord(P[i]) - 64)
    if R_list[i] < 1:
        R_list[i] += 26

for i in range(1, Pn + 1):
    if Pn % i != 0:
        continue
    tmp = R_list[0:i]
    for j in range(i, Pn, i):
        if tmp != R_list[j:j+i]:
            break
    else:
        result = tmp
        break

for i in range(len(result)):
    result[i] = chr(result[i] + 64)

print(''.join(result))
