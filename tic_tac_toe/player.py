class Player:
    def __init__(self):
        self.turn = 1

    def take_action(self, env):
        return "do something on the env"

    def update_state_history(self, state):
        return "update state history"

    def update(self, env):
        return "update value function"
