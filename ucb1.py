import numpy as np
import matplotlib.pyplot as plt
from math import log, sqrt


class Bandit:

    def __init__(self, m):
        """
        m = true mean
        mean = estimate of the bandit mean
        N = nr of arm pulls
        upper_limit = initial value for the reward
        """
        self.m = m
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


def run_experiment(m1, m2, m3, upper_limit, N):
    """
    m1, m2, m3 = means of the three bandits to be compared
    N = int, the number of times we pull
    Returns the cumulative average after every play
    """
    b1 = Bandit(m1, upper_limit)
    b2 = Bandit(m2, upper_limit)
    b3 = Bandit(m3, upper_limit)

    bandits = [b1, b2, b3]
    data = np.empty(N)

    for i in range(N):

        # Greedy part - optimistic initial values
        bandits_ucb = [bi.mean + sqrt(log(bi.N)/(N + pow(10, -5)))
                       for bi in bandits]
        target = bandits[np.argmax(bandits_ucb)]

        new_reward = target.pull()
        target.update(new_reward)
        data[i] = new_reward

    cumulative_avg = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_avg)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)

    print(b1.mean)
    print(b2.mean)
    print(b3.mean)


if __name__ == "__main__":
    N = 100000

    plt.figure()
    exp1 = run_experiment(1.0, 2.0, 3.0, 10, N)
    plt.xscale('log')
    plt.legend()
    plt.show()
