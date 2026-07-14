import numpy as np
rng = np.random.default_rng()

import matplotlib.pyplot as plt

#generate a matrix full of 0 and 1 then convert the 0s to -1
def simulation(number_of_tosses, number_of_iteration):
    """
    Simulate multiple random coin flips.

    Logic
    ----------
    Creates a maxtrix of shape (number_of_iteration, number_of_tosses) 
    full of 1s and 0s then convert the 0s into -1
    """

    matrix = rng.integers(2, size = (number_of_iteration, number_of_tosses)) * 2 - 1

    cumsum = np.cumsum(matrix, axis = 1)

    base_value = np.zeros(shape=(number_of_iteration,1))

    cumsum = np.concatenate((base_value, cumsum), axis = 1)

    return cumsum

def plot(number_of_tosses, number_of_iteration):

    cumsum = simulation(number_of_tosses, number_of_iteration)

    x = np.arange(number_of_tosses+1)

    for i in range(number_of_iteration):

        y = cumsum[i,:]
        plt.plot(x, y, label = f"iteration #{i+1}")

    plt.xlabel("number of tosses")
    plt.ylabel("position")
    plt.title("Evolution of Coin Tosses")
    plt.savefig("monte-carlo-coin-flip.png")
    plt.show()

if __name__ == "__main__":
    plot(100, 30)