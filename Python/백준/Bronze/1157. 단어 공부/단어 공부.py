word = input().upper()
word_list = list(set(word))

cnt = []
for w in word_list:
    cnt.append(word.count(w))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])