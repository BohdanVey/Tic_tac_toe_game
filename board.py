"""
Class to generate board
"""


class Board:
    """
    Initialize board
    """
    player = 'х'
    computer = 'o'

    def __init__(self, board):
        """
        Create an empty board
        """
        self.board = board
        self.move = Board.player
        self.last_move = (-1, -1)

    def status(self, main_move=True):
        """
        Return Status of the field at the moment
        :param main_move: Bool
        :return: int
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i]:
                # Because i i element will be in both situation
                if main_move:
                    if self.board[i][i] == Board.player:
                        print("Player Win")
                        return -1
                    print("Computer Win")
                    return 1
                if self.board[i][i] == Board.player:
                    return -1
                return 1

        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
                self.board[2][0] == self.board[1][1] == self.board[0][2]:
            if self.board[1][1] == Board.player:
                if main_move:
                    print("Player Win")
                return -1
            if main_move:
                print("Computer Win")
            return 1
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return 0
        if main_move:
            print("Draw")
            return 2
        return 0
    def print_board(self):
        """
        Print situation on a board
        :return: None
        """
        print('\n'.join([''.join(x) for x in self.board]))
