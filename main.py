import numpy as np
rng = np.random.default_rng()

# 0 = tails, 1 = head
def flip_a_coin():
   
    a = rng.integers(2)

    return a

def simulation(number_of_tosses):

    toss_count = 0
    head_count = 0

    results = np.empty(number_of_tosses, dtype=int)
    average_evolution = np.empty(number_of_tosses)

    for i in range(number_of_tosses):
        
        toss_count +=1

        result = flip_a_coin()
        results[i] = result

        if result == 1:
            head_count += 1

        average_evolution[i] = head_count / toss_count

    return results, average_evolution

