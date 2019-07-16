#! -*- coding:utf-8 -*-

import os

class TestKnightPatro(object):
    def __init__(self, psize):
        self.psize = psize
        self.board = [[0] * psize for _ in range(psize)]
        self.total = 0

    def print_board(self):
        os.system("clear")
        for i in range(self.psize):
            for j in range(self.psize):
                print(str(self.board[i][j]).center(4), end='')
            print()

    def knight_patrol(self, crow, ccol, step=1):
        if crow >=0 and crow < self.psize and \
            ccol >= 0 and ccol < self.psize and \
            self.board[crow][ccol] == 0:
            self.board[crow][ccol] = step

            if step == self.psize ** 2:
                self.total += 1
                print("%d plan" % self.total)
                self.print_board()

            self.knight_patrol(crow-2, ccol-1, step+1)
            self.knight_patrol(crow-1, ccol-2, step+1)
            self.knight_patrol(crow-2, ccol+1, step+1)
            self.knight_patrol(crow-1, ccol+2, step+1)
            self.knight_patrol(crow+1, ccol+2, step+1)
            self.knight_patrol(crow+2, ccol+1, step+1)
            self.knight_patrol(crow+1, ccol-2, step+1)
            self.knight_patrol(crow+2, ccol-1, step+1)
            #与这个点相关的全部走法遍历完全后，清除这个点的状态
            self.board[crow][ccol] = 0
            self.print_board()


if __name__ == "__main__":
    tk = TestKnightPatro(5)
    tk.knight_patrol(0,0)