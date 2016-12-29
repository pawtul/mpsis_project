import numpy as np

from generators import generate_random_matrix
from solvers import BruteForceSolver, IterativeSolver


if __name__ == "__main__":
    n = 10
    matrix = generate_random_matrix(n)
    # matrix = np.matrix([[0, 1, 0, 0, 0],
                        # [1, 0, 1, 1, 0],
                        # [0, 1, 0, 1, 0],
                        # [0, 1, 1, 0, 1],
                        # [0, 0, 0, 1, 0]])
    solutions_bf = [BruteForceSolver(matrix, i).solve() for i in range(1, n-1)]
    solutions_iter = [IterativeSolver(matrix, i).solve() for i in range(1, n-1)]

    # solution = BruteForceSolver(matrix, 1).solve()
    # solution2 = BruteForceSolver(matrix, 2).solve()

    print(matrix)
    # print solution
    # print solution2
    for bf, it in zip(solutions_bf, solutions_iter):
        print("brute force:")
        print(bf)
        print("-" * 15)
        print("iterative")
        print(it)
        print("-" * 15)

