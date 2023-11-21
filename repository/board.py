import numpy as np
import pygame

SQUARE_SIZE = 100
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Board:
    def __init__(self, rows : int = 6, columns : int = 7):
        self._rows = rows
        self._columns = columns
        self._board = np.zeros((rows, columns))
        self._width = columns * SQUARE_SIZE
        self._height = (rows + 1) * SQUARE_SIZE
        self._screen_size = (self._width, self._height)
        self._screen = pygame.display.set_mode(self._screen_size)

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def screen(self):
        return self._screen

    def on_board(self, column : int):
        return 0 <= column < self._columns

    def is_occupied(self, row : int, column : int):
        """
        checks if a certain spot is occupied
        """
        return self._board[row][column] in [1, 2]

    def game_won(self):
        """
        checks if the game is won
        returns the circle of the winner if the game is won and False otherwise
        """
        for row in range(self.rows - 3):
            for column in range(self.columns):
                if self._board[row][column] == self._board[row + 1][column] == self._board[row + 2][column] == self._board[row + 3][column] and self.is_occupied(row, column):
                    return self._board[row][column]

        for row in range(self.rows):
            for column in range(self.columns - 3):
                if self._board[row][column] == self._board[row][column + 1] == self._board[row][column + 2] == self._board[row][column + 3] and self.is_occupied(row, column):
                    return self._board[row][column]

        for row in range(self.rows - 3):
            for column in range(self.columns - 3):
                if self._board[row][column] == self._board[row + 1][column + 1] == self._board[row + 2][column + 2] == self._board[row + 3][column + 3] and self.is_occupied(row, column):
                    return self._board[row][column]

        for row in range(self.rows - 3):
            for column in range(self.columns - 1, 3, -1):
                if self._board[row][column] == self._board[row + 1][column - 1] == self._board[row + 2][column - 2] == self._board[row + 3][column - 3] and self.is_occupied(row, column):
                    return self._board[row][column]
        return False

    def game_draw(self):
        """
        checks if the game is a draw
        returns True if the game is a draw and False otherwise
        """
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column] == 0:
                    return False
        return True

    def is_legal_move(self, column : int):
        """
        checks if the move is legal for a given state of a board and a column
        returns True if the move is legal and False otherwise
        """
        for row in range(self.rows - 1, -1, -1):
            if self._board[row][column] == 0:
                return True
        return False

    def move(self, circle : int, column : int):
        """
        if possible, makes a move and returns True
        otherwise it throws an error
        """
        if self.is_legal_move(column):
            for i in range(self.rows - 1, -1, -1):
                if self._board[i][column] == 0:
                    self._board[i][column] = circle
                    return True
        return False

    def simulate_move(self, circle : int, given_column : int):
        simulated_board = Board(self.rows, self.columns)
        for row in range(simulated_board.rows):
            for column in range(simulated_board.columns):
                simulated_board._board[row][column] = self._board[row][column]
        if simulated_board.move(circle, given_column):
            return simulated_board
        return False

    def draw(self):
        pygame.draw.rect(self._screen, BLUE, (0, SQUARE_SIZE, SQUARE_SIZE * self.columns, SQUARE_SIZE * self.rows))
        for row in range(self.rows):
            for column in range(self.columns):
                if self._board[row][column] == 0:
                    pygame.draw.circle(self._screen, BLACK, (int(column * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE * 3 // 2)), SQUARE_SIZE // 2)
                elif self._board[row][column] == 1:
                    pygame.draw.circle(self._screen, GREEN, (int(column * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE * 3 // 2)), SQUARE_SIZE // 2)
                elif self._board[row][column] == 2:
                    pygame.draw.circle(self._screen, RED, (int(column * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE * 3 // 2)), SQUARE_SIZE // 2)
        pygame.display.update()
