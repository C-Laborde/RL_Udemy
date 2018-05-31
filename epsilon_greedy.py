import numpy as np
import random
import matplotlib.pyplot as plt


class Bandit:

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


def run_experiment(m1, m2, m3, eps, N):
    """
    m1, m2, m3 = means of the three bandits to be compared
    eps = epsilon for Epsilon-Greedy
    N = int, the number of times we pull
    Returns the cumulative average after every play
    """
    b1 = Bandit(m1)
    b2 = Bandit(m2)
    b3 = Bandit(m3)

    bandits = [b1, b2, b3]
    data = np.empty(N)

    for i in range(N):
        p = np.random.random()

        # Epsilon - Greedy part
        if p < eps:
            chosen = random.choice([0, 1, 2])
            target = bandits[chosen]
        else:
            bandits_means = [bi.mean for bi in bandits]
            target = bandits[np.argmax(bandits_means)]

        new_reward = target.pull()
        target.update(new_reward)
        data[i] = new_reward

    cumulative_avg = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_avg, label="eps = " + str(eps))
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)

    print(b1.mean)
    print(b2.mean)
    print(b3.mean)


if __name__ == "__main__":
    N = 100000

    plt.figure()
    exp1 = run_experiment(2.0, 2.0, 1.0, 0.1, N)
    exp2 = run_experiment(2.0, 2.0, 1.0, 0.05, N)
    exp3 = run_experiment(2.0, 2.0, 1.0, 0.01, N)
    plt.xscale('log')
    plt.legend()
    plt.show()
