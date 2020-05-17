import numpy as np
from config import LENGTH


class Player:
    def __init__(self, verbose=False, eps=0.1, alpha=0.5):
        self.eps = eps  # Prob of choosing random action instead of greedy
        self.alpha = alpha  # Learning rate for the update equation
        self.verbose = verbose
        self.state_history = []
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
        self.sym = symbol

    def set_verbose(self, verbose=False):
        """
        Prints out additional info
        """
        self.verbose = verbose

    def reset_history(self):
        """
        Once the episode is finished we don't need the history anymore. The
        history is reseted before starting a new episode
        """
        self.state_history = []

    def take_action(self, env):
        """
         Choose an action based on epsilon-greedy strategy
        """
        p = np.random.rand()
        best_state = None
        if p < self.eps:
            # Take a random action
            if self.verbose:
                print("Taking a random action")

            possible_moves = []
            for i in range(LENGTH):
                for j in range(LENGTH):
                    if env.is_empty(i, j):
                        possible_moves.append((i, j))
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]

        else:
            # Greedy action of the strategy. Choose the best action based on
            # current values of states, loop through all possible moves, get
            # their values, keep track of the best value
            pos2value = {}  # For debugging
            next_move = None
            best_value = -1
            for i in range(LENGTH):
                for j in range(LENGTH):
                    if env.is_empty(i, j):
                        # What is the state if we made this move?
                        env.board[i, j] = self.sym
                        state = env.get_state()
                        env.board[i, j] = 0
                        pos2value[(i, j)] = self.V[state]
                        if self.V[state] > best_value:
                            best_value = self.V[state]
                            best_state = state
                            next_move = (i, j)

            if self.verbose:
                print("Taking a greedy action")
                for i in range(LENGTH):
                    print("-----------------")
                    for j in range(LENGTH):
                        if env.is_empty(i, j):
                            # print the value
                            # Print(f"{pos2value[(i, j)%.2f]}|")
                            print(" %.2f|" % pos2value[(i,j)], end="")
                        else:
                            print(" ", end="")
                            if env.board[i, j] == env.x:
                                print("x |", end="")
                            elif env.board[i, j] == env.o:
                                print("o |", end="")
                            else:
                                print(" |", end="")
                    print("")
                print("-----------------")

        # Make the move
        env.board[next_move[0], next_move[1]] = self.sym

    def update_state_history(self, state):
        """
        We can't include this in take_action because take_action only happens
        once every other iteration fo each player
        state_history needs to be updated every iteration
        """
        self.state_history.append(state)
        return "update state history"

    def update(self, env):
        """
        We want to backtrack over the states, so that:
        V(prev_state) = V(prev_state) + alpha(V(next_state) - V(prev_state))
        where V(next_state) = reward if it's the most current state

        We only do this at the end of the episode, not so for other algorithms
        """
        reward = env.reward(self.sym)
        target = reward
        for prev in reversed(self.state_history):
            value = self.V[prev] + self.alpha * (target - self.V[prev])
            self.V[prev] = value
            target = value
        self.reset_history()
