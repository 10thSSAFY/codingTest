def count_lucky_permutations(s):
    chars = sorted(s)  # 입력 문자열 정렬
    used = [False] * len(chars)
    return generate_permutations(chars, "", used, '\0')


def generate_permutations(chars, current, used, last_char):
    if len(current) == len(chars):
        return 1

    cnt = 0
    for i in range(len(chars)):
        # 인접한 문자열이 다른 행운 문자열을 구성해야 합니다. 이전 문자와 동일하면 비교할 필요가 없습니다.
        if used[i] or (i > 0 and chars[i] == chars[i - 1] and not used[i - 1]):
            continue
        # 추가될 문자와 생성된 순열의 마지막 글자가 같다면 의미없겠죠?
        if len(current) > 0 and chars[i] == last_char:
            continue

        used[i] = True
        # 현재 문자를 추가하여 다시 순열을 생성
        cnt += generate_permutations(chars, current + chars[i], used, chars[i])
        used[i] = False

    return cnt

# 입력
s = input().strip()

# 결과 출력
result = count_lucky_permutations(s)
print(result)
