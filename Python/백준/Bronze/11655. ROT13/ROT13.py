S = input()

result = ''
for ch in S:
    if 'a' <= ch <= 'z':
        ch = ord(ch) + 13
        if ch > 122:
            ch -= 26
        result += chr(ch)

    elif 'A' <= ch <= 'Z':
        ch = ord(ch) + 13
        if ch > 90:
            ch -= 26
        result += chr(ch)

    else:
        result += ch

print(result)