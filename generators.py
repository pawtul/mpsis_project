from random import randint

import numpy as np

def generate_random_matrix(n):
    mat = np.zeros((n, n))
    for i in range(n-1):
        for k in range(i+1, n):
            mat[i, k] = mat[k, i] = randint(0, 1)
    return mat


def generate_files_with_matrix(n, filename):
    mat = generate_random_matrix(n)
    cplex_mat = mat + np.eye(n)
    with open(filename+'.mod') as file:
        file.write("mat = " + str(cplex_mat) + ";")

    with open(filename+'.py') as file:
        file.write("mat = " + str(mat))

