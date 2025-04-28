lv, score = input().split()

if score == 'miss':
    print(0)
elif score == 'bad':
    print(200 * int(lv))
elif score == 'cool':
    print(400 * int(lv))
elif score == 'great':
    print(600 * int(lv))
elif score == 'perfect':
    print(1000 * int(lv))