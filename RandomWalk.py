import random

import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, dimensions, staps):
        self.dim = dimensions
        self.staps = staps
        self.sistem = [[0 for stap in range(self.staps)] for dim in range(self.dim)]

    def walk(self):
        for stap in range(self.staps):
            random_dim = random.Randint(0, self.dim - 1)
        for dim in range(self.dim):
            if dim == random_dim:
                pass
            else:
                pass

    def move(self, dim, step):
        diraction = 1
        coin_flit = random.random()
        if coin_flit < 0.5:
            diraction = -1
        self.coordinate_system[dim][step]