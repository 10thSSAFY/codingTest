IPv6 = input()
N = len(IPv6)

result = [[] for _ in range(8)]
idx = 0
hexa = ''
for i in range(N):
    if IPv6[i : i+2] == '::':
        break

    if IPv6[i] == ':':
        result[idx].append(hexa)
        hexa = ''
        idx += 1
        continue

    hexa = hexa + IPv6[i]

if hexa:
    result[idx].append(hexa)

if idx != 7:
    idx = 7
    hexa = ''
    for i in range(N, -1, -1):
        if IPv6[i-2 : i] == '::':
            break

        if IPv6[i-1] == ':':
            result[idx].append(hexa)
            hexa = ''
            idx -= 1
            continue

        hexa = IPv6[i-1] + hexa

if hexa:
    result[idx].append(hexa)

for i in range(8):
    if not result[i]:
        print('0000', end='')
    else:
        hexa = result[i][0]
        print(f'{hexa:0>4}', end='')
    if i != 7:
        print(':', end='')