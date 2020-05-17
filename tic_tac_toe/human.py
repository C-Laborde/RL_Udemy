class Human:
    def __init__(self):
        pass

    def set_symbol(self, symbol):
        self.sym = symbol

    def take_action(self, env):
        while True:
            # Break if we make a legal move
            move = input("Enter coordinates i, j for your next move (i,j=0..2): ")
            try:
                i, j = move.split(",")
            except ValueError:
                print("Wrong specification of move. Use format i,j")
                continue
            try:
                i = int(i)
                j = int(j)
            except ValueError:
                print("Invalid move, coordinate not an integer")
                continue
            if not (0 <= i <= 2) and (0 <= j <= 2):
                print("i, j must be between 0 and 2")
                continue
            if env.is_empty(i, j):
                env.board[i, j] = self.sym
                break
            else:
                print(f"Position ({i}, {j}) is not empty")

    def update(self, env):
        pass

    def update_state_history(self, state):
        pass
