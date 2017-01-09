import argparse

import numpy as np

from utils import check_and_prepare_matrix

from generators import generate_random_matrix
from solvers import BruteForceSolver, IterativeSolver, ReverseIterativeSolver

import cutMatrix


parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, default=5, help='number of nodes', dest='n')


if __name__ == "__main__":
    # args = parser.parse_args()
    # n = args.n

    # matrix = generate_random_matrix(n)
    n = cutMatrix.d
    matrix = check_and_prepare_matrix(np.matrix(cutMatrix.mat))
    # matrix = np.ones((n, n)) - np.eye(n)
    # matrix = np.matrix([[0, 1, 0, 0, 0],
                        # [1, 0, 1, 1, 0],
                        # [0, 1, 0, 1, 0],
                        # [0, 1, 1, 0, 1],
                        # [0, 0, 0, 1, 0]])
    # solutions_bf = [BruteForceSolver(matrix, i).solve() for i in range(1, n-1)]
    # solutions_iter = [IterativeSolver(matrix, i).solve() for i in range(1, n-1)]
    # solutions_reviter = [ReverseIterativeSolver(matrix, i).solve() for i in range(1, n-1)]

    solutions_bf = [BruteForceSolver(matrix, n).solve()]
    solutions_iter = [IterativeSolver(matrix, n).solve()]
    solutions_reviter = [ReverseIterativeSolver(matrix, n).solve()]

    print(matrix)

    solutions = {
            'bf:' : solutions_bf,
            'iter: ': solutions_iter,
            'rev iter: ': solutions_reviter
            }

    for i in range(n-2):
        print '='*10, i, '='*10
        for solution_name in solutions:
            print(solution_name)
            print(solutions[solution_name][i])
            print('-'*20)

