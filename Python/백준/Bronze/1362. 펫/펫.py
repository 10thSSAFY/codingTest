cnt = 0
while 1:
    death = 0
    cnt += 1

    o, w = map(int,input().split())
    if o == w == 0:
        break

    while 1:
        a,b = input().split()
        if a == '#' and b == '0':
            break
        b = int(b)
        if a == 'F':
            w = w + b
        elif a == 'E':
            w = w - b
        if w <= 0 :
            death = 1
    print(cnt,end=' ')

    if death == 1:
        print("RIP")
    else:
        if o/2 < w < o*2:
            print(":-)")
        else:
            print(":-(")
