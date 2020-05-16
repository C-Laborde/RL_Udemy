import numpy as np


class Environment:
    def __init__(self):
        self.game_over = False
        self.length = 3
        self.board = np.zeros(self.length, self.length)
        self.x = 1   # represents and x on the board, player 1
        self.o = -1  # represents and o on the board, player 2
        self.winner = None
        # self.map = {0: 0, "x": 1, "o": 2}
        self.state = None
        self.num_states = 3 ** (self.length * self.length)

    def game_over(self, force_recalculate=False):
        if not force_recalculate:
            return self.game_over
        if 0 not in self.board or self.winner_exists():
            return True
        return False

    def draw_board(self):
        return None

    def get_state(self):
        # base 3 representation of the state
        k = 0
        hash_ = 0
        for i in range(self.length):
            for j in range(self.length):
                v = self.board[i, j]
                hash_ += (3**k) * v
                k += 2
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

    def is_empty(self, i, j):
        return self.board[i, j] == 0
    
    def reward(self, symbol):
        return