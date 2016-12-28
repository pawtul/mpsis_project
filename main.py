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

    # solution = BruteForceSolver(matrix, 1).solve()
    # solution2 = BruteForceSolver(matrix, 2).solve()

    print(matrix)
    # print solution
    # print solution2
    solver_iter = IterativeSolver(matrix, 1)
    for i in range(n-2):
        print("brute force:")
        print(solutions_bf[i])
        print("-" * 15)
        print("iterative")
        solver_iter.number_to_remove = i
        solution = solver_iter.solve()
        print(solution)
        print("-" * 15)

