class Environment:
    def __init__(self):
        self.game_over = False
        self.length = 3
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.x = 1
        self.o = 2
        self.map = {"0": 0, "x": 1, "o": 2}
        self.state = None

    def game_over(self):
        return "True or False"

    def draw_board(self):
        return None

    def get_state(self):
        # base 3 representation of the state
        k = 0
        hash_ = 0
        for i in range(self.length):
            for j in range(self.length):
                v = self.map.get(self.board[i, j])
                hash_ += (3**k) * v
                k += 2
        return hash_
