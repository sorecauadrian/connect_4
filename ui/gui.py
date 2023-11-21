import sys
import pygame
from repository.board import Board
from service.game import Player, Computer

SQUARE_SIZE = 100
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("connect four")
font = pygame.font.Font(None, 25)

class GUI:
    def __init__(self, board : Board = Board(), player : Player = Player(), computer : Computer = Computer()):
        self._board = board
        self._player = player
        self._computer = computer

    def start(self):
        # turn == True => player's turn
        # turn == False => computer's turn
        turn = True
        self._board.draw()
        while True:
            winner = self._board.game_won()
            if winner is not False:
                if winner == 1:
                    label = font.render("you won!", True, GREEN)
                    self._board.screen.blit(label, (40, 10))
                elif winner == 2:
                    label = font.render("you lost!", True, GREEN)
                    self._board.screen.blit(label, (40, 10))
                pygame.time.wait(1000)
                exit()
            elif self._board.game_draw():
                if not turn:
                    self._board.draw()
                exit()

            if turn:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                    elif event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(self._board.screen, BLACK, (0, 0, self._board.columns * SQUARE_SIZE, SQUARE_SIZE))
                        column = event.pos[0] // SQUARE_SIZE
                        pygame.draw.circle(self._board.screen, GREEN, (column * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 2)
                        pygame.display.update()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            column = event.pos[0] // SQUARE_SIZE
                            self._board.move(1, column)
                            turn = not turn
            else:
                self._computer.play(self._board)
                turn = not turn
                self._board.draw()


gui = GUI()
gui.start()
