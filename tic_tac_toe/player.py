class Player:
    def __init__(self, eps=0.1, alpha=0.5):
        self.eps = eps  # Prob of choosing random action instead of greedy
        self.alpha = alpha  # Learning rate for the update equation
        self.verbose = False
        self.state_hisotry = []
        self.turn = 1

    def setV(self, V):
        """
        Initializes the value function
        """
        self.V = V
    
    def set_symbol(self, symbol):
        """
        Assigns symbol to agent to use in the board
        """
        self.sym = sym
    
    def set_verbose(self, verbose=False):
        """
        Prints out additional info
        """
        self.verbose = v

    def reset_history(self):
        """
        Once the episode is finished we don't need the history anymore. The
        history is reseted before starting a new episode 
        """
        self.state_hisotry = []
    
    def take_action(self, env):
        return "do something on the env"

    def update_state_history(self, state):
        return "update state history"

    def update(self, env):
        return "update value function"
