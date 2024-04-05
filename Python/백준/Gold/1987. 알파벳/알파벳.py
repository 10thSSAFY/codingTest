import os
import io
speed_input = io.BytesIO(os.read(0, os.fstat(0).st_size))


class Solver:
    def __init__(self):
        self.r, self.c = map(int, speed_input.readline().split())
        self.max_depth = 0
        self.board = []
        for _ in range(self.r):
            self.board.extend(map(lambda ch: 1 << ch - 65, speed_input.readline().rstrip()))

    def __get_adj(self, cur_pos):
        i = cur_pos // self.c
        j = cur_pos % self.c

        adj = []
        if i > 0:
            adj.append(cur_pos - self.c)
        if j > 0:
            adj.append(cur_pos - 1)
        if i < self.r - 1:
            adj.append(cur_pos + self.c)
        if j < self.c - 1:
            adj.append(cur_pos + 1)
        return adj

    def search(self):
        pos_set = {0}
        visited = [set() for _ in range(self.r * self.c)]
        visited[0].add(self.board[0])
        for depth in range(26+1):
            if depth >= 26 or not pos_set:
                self.max_depth = depth
                break

            new_pos_set = set()
            new_visited = [set() for _ in range(len(visited))]
            while pos_set:
                cur_pos = pos_set.pop()
                for neighbor_pos in self.__get_adj(cur_pos):
                    neighbor_alpha = self.board[neighbor_pos]
                    flag = True
                    for visited_alpha in visited[cur_pos]:
                        if not neighbor_alpha & visited_alpha:
                            new_visited[neighbor_pos].add(visited_alpha | neighbor_alpha)
                            if flag:
                                new_pos_set.add(neighbor_pos)
                                flag = False

            pos_set = new_pos_set
            visited = new_visited

    def solve(self):
        self.search()
        print(self.max_depth)


if __name__ == '__main__':
    Solver().solve()