import numpy as np


"""
mu is no longer something for which we're trying to find a fix estimate of,
it's a random variable whose distribution has fixed parameters
"""


class BayesianBandit:

    def __init__(self, m):
        self.m = m
        # parameters for mu prior are N(0, 1)
        self.m0 = 0
        self.lambda0 = 1
        self.sum_x = 0   # the posterior depends on the sum of x
        self.tau = 1

    def pull(self):
        return np.random.randn() + self.m

    def sample(self):
        """
        Generates a sample from a Gaussian with mean m0 and precision lambda0
        """
        return np.random.randn()/np.sqrt(self.lambda0) + self.m0

    def update(self, x):
        # assume tau is 1
        self.lambda0 += 1
        self.sum_x += x
        self.m0 = self.tau*self.sum_x / self.lambda0
