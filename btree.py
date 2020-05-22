"""
Binary tree implementation
"""
from bt_node import Node


class BinaryTree:
    """
    Class representing a Binary Tree
    """

    def __init__(self, board):
        """
        Initialize Tree
        :param board: list of list

        """
        self.root = Node(board)

    def get_best_move(self, move):
        """
        Get best move strategy
        :param move: char
        :return: None
        """
        return self.root.best_strategy(move)

    def find(self, value):
        """
        The future function
        :param value: list
        :return: None
        """
        raise NotImplementedError
