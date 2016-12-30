import argparse

import numpy as np

from generators import generate_random_matrix
from solvers import BruteForceSolver, IterativeSolver, ReverseIterativeSolver


parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, default=5, help='number of nodes', dest='n')


if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n

    matrix = generate_random_matrix(n)
    # matrix = np.matrix([[0, 1, 0, 0, 0],
                        # [1, 0, 1, 1, 0],
                        # [0, 1, 0, 1, 0],
                        # [0, 1, 1, 0, 1],
                        # [0, 0, 0, 1, 0]])
    solutions_bf = [BruteForceSolver(matrix, i).solve() for i in range(1, n-1)]
    solutions_iter = [IterativeSolver(matrix, i).solve() for i in range(1, n-1)]
    solutions_reviter = [ReverseIterativeSolver(matrix, i).solve() for i in range(1, n-1)]

    # solution = BruteForceSolver(matrix, 1).solve()
    # solution2 = BruteForceSolver(matrix, 2).solve()

    print(matrix)
    # print solution
    # print solution2
    solutions = {
            'bf:' : solutions_bf,
            'iter: ': solutions_iter,
            'rev iter: ': solutions_reviter
            }

    for i in range(n-2):
        print('='*20)
        for solution_name in solutions:
            print(solution_name)
            print(solutions[solution_name][i])
            print('-'*20)

    # for bf, it in zip(solutions_bf, solutions_iter):
        # print("brute force:")
        # print(bf)
        # print("-" * 15)
        # print("iterative")
        # print(it)
        # print("-" * 15)

