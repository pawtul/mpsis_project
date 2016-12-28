from random import randint

import numpy as np

def generate_random_matrix(n):
    mat = np.zeros((n, n))
    for i in range(n-1):
        for k in range(i+1, n):
            mat[i, k] = mat[k, i] = randint(0, 1)
    return mat

