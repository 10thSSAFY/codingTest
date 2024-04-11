def main():
    Min, Max = map(int, input().split())
    Check = [1] * (Max - Min + 1)
    
    for i in range(2, int(Max**(0.5) + 1)):
        pow = i*i
        start_index = Min // pow
        if Min % pow != 0:
            start_index += 1
        for j in range(start_index, Max // pow + 1):
            Check[int((j * pow) - Min)] = 0
    return sum(Check)

print(main())