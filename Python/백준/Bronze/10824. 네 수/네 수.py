A = 0
B = 0
C = 0
D = 0


class Calculate:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        res = int(str(self.num) + str(other.num))
        return res


def main():
    global A, B, C, D
    A, B, C, D = map(int, input().split())
    add1 = Calculate(A) + Calculate(B)
    add2 = Calculate(C) + Calculate(D)
    print(add1 + add2)


if __name__ == '__main__':
    main()
