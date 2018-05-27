import numpy as np
import matplotlib.pyplot as pyplot


class Bandit(self, m):

    def __init__(self, m):
        """
        m = true mean
        mean = estimate of the bandit mean
        N = nr of arm pulls
        """
        self.m = m
        self.mean = 0
        self.N = 0

    def pull(self):
        """
        Returns the bandit reward: a sample (or samples)from the “standard
        normal” distribution sampled from a univariate “normal” (Gaussian)
        distribution of mean 0 and variance 1"""
        return np.random().randn() + self.m
