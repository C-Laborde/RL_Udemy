import numpy as np


class Bandit:

    def __init__(self, m, eps=None, upper_limit=None, method="eps"):
        """
        m = true mean
        mean = estimate of the bandit mean
        N = nr of arm pulls
        """
        self.m = m

        if method == "eps":
            try:
                float(eps)
                self.mean = 0
                self.N = 0
            except TypeError:
                print("For using Epsilon-Greedy you have to define epsilon")
                raise
        elif method == "upper_limit":
            try:
                float(upper_limit)
                self.mean = upper_limit
                self.N = 1
            except TypeError:
                print("For using Optimal Initial Value method you have to " +
                      "choose an initial value for the reward")
                raise
        elif method == "ucb1":
            self.mean = 0
            self.N = 1

    def pull(self):
        """
        Returns the bandit reward: a sample (or samples) from the “standard
        normal” distribution sampled from a univariate “normal” (Gaussian)
        distribution of mean 0 and variance 1"""
        return np.random.randn() + self.m

    def update(self, x):
        """
        Updates the rewards mean based on the latest sample received from the
        Bandit
        """
        self.N += 1
        self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N * x
