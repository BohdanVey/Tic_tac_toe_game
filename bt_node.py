"""
Binary tree Node
"""
import copy
import random
from board import Board


class Node:
    """
    Class representing a Node for tic-tac-toe
    """

    def __init__(self, data):
        """
        Initialize Node
        :param data: list of list
        """
        self.data = copy.deepcopy(data)
        self.left = None
        self.right = None

    def get_random_move(self):
        """
        Get random free move
        :return: x,y
        """
        pos_x, pos_y = random.randint(0, 2), random.randint(0, 2)
        if self.data.board[pos_x][pos_y] != ' ':
            return self.get_random_move()
        return pos_x, pos_y

    def best_strategy(self, move):
        """
        Get best strategy beside two randomly generated
        :return: int,int,int,int
        """
        for i in range(9):
            if self.data.board[i // 3][i % 3] == ' ':
                break
            if i == 8:
                return 0, 0, 0, 0
        x_1, y_1 = self.get_random_move()
        tries = 0
        while tries < 10:
            x_2, y_2 = self.get_random_move()
            tries += 1
            if x_1 != x_2 or y_1 != y_2:
                break
        self.data.board[x_1][y_1] = move
        status1 = self.data.status(False)
        if status1 == 1:
            return x_1, y_1, status1, 0
        self.data.board[x_1][y_1] = ' '
        self.data.board[x_2][y_2] = move
        status2 = self.data.status(False)
        if status2 == 1:
            return x_2, y_2, status2, 0
        if status1 != -1:
            # Return To previous position
            self.data.board[x_2][y_2] = ' '
            self.data.board[x_1][y_1] = move
            if move == Board.computer:
                status1 -= self.best_strategy(Board.player)[2] + \
                           self.best_strategy(Board.player)[3]
            else:
                status1 -= self.best_strategy(Board.computer)[2] + \
                           self.best_strategy(Board.computer)[3]

        if status2 != -1:
            self.data.board[x_1][y_1] = ' '
            self.data.board[x_2][y_2] = move
            if move == Board.computer:
                status2 -= self.best_strategy(Board.player)[2] + \
                           self.best_strategy(Board.player)[3]
            else:
                status2 -= self.best_strategy(Board.computer)[2] + \
                           self.best_strategy(Board.computer)[3]

        self.data.board[x_2][y_2] = ' '
        self.data.board[x_1][y_1] = ' '
        if status1 > status2:
            return x_1, y_1, status1, status2
        return x_2, y_2, status2, status1
