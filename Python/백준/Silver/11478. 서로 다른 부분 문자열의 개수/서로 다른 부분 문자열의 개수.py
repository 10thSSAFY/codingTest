text = input()
set_lst = set()

for i in range(len(text)):
    for j in range(i, len(text)):
        set_lst.add(text[i:j+1])
        
print(len(set_lst))