N = 0


class Calculate:
    def __init__(self, num):
        self.num = str(num)

    def digit_product(self, part):
        curr_mul = 1
        for digit in part:
            curr_mul *= int(digit)
        return curr_mul

    def is_collect(self):
        length = len(self.num)

        for i in range(1, length):
            part1 = self.num[:i]
            part2 = self.num[i:]

            curr_mul1 = self.digit_product(part1)
            curr_mul2 = self.digit_product(part2)

            if curr_mul1 == curr_mul2:
                return True

        return False


def main():
    global N
    N = int(input())
    yujin = Calculate(N)

    if yujin.is_collect():
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
