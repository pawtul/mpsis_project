import argparse

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
    for i in range(n):
        if not sum(mat[i]):
            return generate_files_with_matrix(n, filename)

    with open(filename+'.mod', "w") as file:
        file.write("mat = " + str(cplex_mat) + ";")

    with open(filename+'.py', "w") as file:
        file.write("mat = " + str(mat))

parser = argparse.ArgumentParser("Generates file of matrices")
parser.add_argument("-n", dest='n', type=int)
parser.add_argument("-f", dest="f")

if __name__ == "__main__":
    args = parser.parse_args()
    generate_files_with_matrix(args.n, args.f)

