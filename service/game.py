from repository.board import Board
import random


class Player:
    pass


class Computer:
    def __init__(self, circle : int = 2, opponent_circle : int = 1):
        self._circle = circle
        self._opponent_circle = opponent_circle

    def play(self, board: Board):
        available_columns = []
        for column in range(board.columns):
            if board.is_legal_move(column):
                available_columns.append(column)
        for column in available_columns:
            if board.simulate_move(self._circle, column).game_won() or board.simulate_move(self._opponent_circle, column).game_won():
                board.move(self._circle, column)
                return True
        board.move(self._circle, available_columns[random.randint(0, len(available_columns) - 1)])
        return True