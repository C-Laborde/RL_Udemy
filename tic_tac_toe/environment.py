import numpy as np
from config import LENGTH


class Environment:
    def __init__(self):
        self.ended = False
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = 1   # represents and x on the board, player 1
        self.o = -1  # represents and o on the board, player 2
        self.winner = None
        self.state = None
        self.num_states = 3 ** (LENGTH * LENGTH)

    def game_over(self, force_recalculate=False):
        """
        Returns True if game over (there's a winner or a draw), otherwise False
        """
        if not force_recalculate and self.ended:
            return self.ended

        # Rows check
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # Columns check
        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # Check left to right diagonal
        for player in (self.x, self.o):
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True

        # Check right to left diagonal
        if np.fliplr(self.board).trace() == player*LENGTH:
            self.winner = player
            self.ended = True
            return True

        # Check draw
        if 0 not in self.board:
            self.winner = None
            self.ended = True
            return True

        self.winner = None
        return False

    def draw_board(self):
        for i in range(LENGTH):
            print("-----------------")
            for j in range(LENGTH):
                # print(" ", end="")
                if self.board[i, j] == self.x and j != 2:
                    print("  x  |", end="")
                elif self.board[i, j] == self.x and j == 2:
                    print("  x  ", end="")
                elif self.board[i, j] == self.o and j != 2:
                    print("  o  |", end="")
                elif self.board[i, j] == self.o and j == 2:
                    print("  o  ", end="")
                elif j != 2:
                    print("     |", end="")
                else:
                    print("    ", end="")
            print("")
        print("-----------------")

    def get_state(self):
        # base 3 representation of the state
        k = 0
        hash_ = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i, j] == 0:
                    v = 0
                elif self.board[i, j] == self.x:
                    v = 1
                if self.board[i, j] == self.o:
                    v = 2
                hash_ += (3**k) * v
                k += 1
        return hash_

    def is_empty(self, i, j):
        return self.board[i, j] == 0

    def reward(self, sym):
        # No reward until the game is over
        if not self.game_over():
            return 0
        # If we get here, game is over
        # sym will be self.x o self.o
        return 1 if self.winner == sym else 0
