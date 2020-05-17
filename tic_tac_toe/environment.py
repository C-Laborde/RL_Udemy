import numpy as np
from config import LENGTH


class Environment:
    def __init__(self):
        self.ended = False
        self.board = np.zeros(LENGTH, LENGTH)
        self.x = 1   # represents and x on the board, player 1
        self.o = -1  # represents and o on the board, player 2
        self.winner = None
        # self.map = {0: 0, "x": 1, "o": 2}
        self.state = None
        self.num_states = 3 ** (LENGTH * LENGTH)

    def game_over(self, force_recalculate=False):
        if not force_recalculate and self.ended:
            return self.ended
        # TODO I'm not checking anywhere if there's a draw!
        if 0 not in self.board or self.winner_exists():
            return True
        return False

    def draw_board(self):
        for i in range(LENGTH):
            print("--------------")
            for j in range(LENGTH):
                print(" ")
                if self.board[i, j] == self.x:
                    print("x")
                elif self.board[i, j] == self.o:
                    print("o")
                else:
                    print(" ")
            print("")
        print("--------------")

    def get_state(self):
        # base 3 representation of the state
        # This only works with self.x 1 y self.o2
        k = 0
        hash_ = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                v = self.board[i, j]
                hash_ += (3**k) * v
                k += 1
        return hash_

    def get_state_course(self):
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

    def winner_exists(self):
        winner_exists = False
        while not winner_exists:
            for i in range(self.lenght):
                if len(set(self.board[i])) == 1:
                    self.winner = set(self.board[i])
                    winner_exists = True
                    break
            for i in range(self.lenght):
                if len(set(self.board[:, i])) == 1:
                    self.winner = set(self.board[:, i])
                    winner_exists = True
                    break
            if self.board[0, 0] == self.board[2, 2] == self.board[2, 2]:
                self.winner = self.board[0, 0]
                winner_exists = True
            if self.board[0, 2] == self.board[2, 2] == self.board[2, 0]:
                self.winner = self.board[0, 2]
                winner_exists = True
        self.game_over = winner_exists
        return winner_exists

    def winner_exists_course(self):
        # This works with self.x = 1 and self.o = -1
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player * LENGTH():
                    self.winner = player
                    self.ended = True
                    return True

        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:, j].sum() == player * LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        for player in (self.x, self.o):
            if self.board.trace() == player * self.lenght:
                self.winner = player
                self.ended = True
                return True

            if np.fliplr(self.board).trace() == player * LENGTH():
                self.winner = player
                self.ended = True
                return True

        if np.all((self.board == 0) == False):
            self.winner = None
            self.ended = True
            return True

        self.winner = None
        return False

    def is_empty(self, i, j):
        return self.board[i, j] == 0

    def reward(self, sym):
        # No reward until the game is over
        if not self.game_over():
            return 0
        # If we get here, game is over
        # sym will be self.x o self.o
        return 1 if self.winner == sym else 0