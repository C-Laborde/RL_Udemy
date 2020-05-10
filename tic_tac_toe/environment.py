class Environment:
    def __init__(self):
        self.game_over = False
        self.length = 3
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.x = 1
        self.o = 2
        # self.map = {0: 0, "x": 1, "o": 2}
        self.state = None

    def game_over(self, force_recalculate=False):
        if 0 not in self.board or self.winner_exists()[1]:
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
        found_winner = False
        winner = None
        while not found_winner:
            for i in range(self.lenght):
                if len(set(self.board[i])) == 1:
                    winner = set(self.board[i])
                    found_winner = True
                    break
            for i in range(self.lenght):
                if len(set(self.board[:, i])) == 1:
                    winner = set(self.board[:, i])
                    found_winner = True
                    break
            if self.board[0, 0] == self.board[2, 2] == self.board[2, 2]:
                winner = self.board[0, 0]
                found_winner = True
            if self.board[0, 2] == self.board[2, 2] == self.board[2, 0]:
                winner = self.board[0, 2]
                found_winner = True
        return (winner, found_winner)
