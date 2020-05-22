"""
The main module to play game
"""

from board import Board
from btree import BinaryTree


def make_move(board):
    """
    Make move
    :return: None
    """
    board.print_board()
    if board.move == Board.player:
        while True:
            pos_x, pos_y = [int(x) for x in input("Enter move coordinate separated"
                                                  " by spaces").split()]
            if 1 <= pos_x <= 3 and 1 <= pos_y <= 3:
                pos_x -= 1
                pos_y -= 1
                if board.board[pos_x][pos_y] == ' ':
                    board.board[pos_x][pos_y] = Board.player
                    break
                else:
                    print("This field isn't empty\n"
                          "Choose another one")
            else:
                print("This coordinates does not exist\n"
                      "print coordinates in range from 1 to 3")
        board.move = Board.computer
    else:
        pos_x, pos_y, _, _ = BinaryTree(board).get_best_move(Board.computer)
        board.board[pos_x][pos_y] = Board.computer
        board.move = Board.player
    if not board.status():
        make_move(board)
    else:
        board.print_board()

if __name__ == '__main__':
    make_move(Board([[' '] * 3 for x in range(3)]))
