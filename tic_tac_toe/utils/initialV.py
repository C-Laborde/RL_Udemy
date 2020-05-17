import numpy as np


def initialV_x(env, state_winner_triples):
    """
    Initialize state values as follows
    - if x wins, V(s) = 1
    - if x loses, V(s) = 0
    - otherwise, V(s) = 0.5
    """
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V


def initialV_o(env, state_winner_triples):
    """
    Initialize state values as follows
    - if o wins, V(s) = 1
    - if o loses, V(s) = 0
    - otherwise, V(s) = 0.5
    """
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V
