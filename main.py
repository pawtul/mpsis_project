import argparse
from datetime import datetime
import json
import re

import numpy as np

from utils import check_and_prepare_matrix
from generators import generate_random_matrix
from solvers import BruteForceSolver, IterativeSolver, ReverseIterativeSolver

parser = argparse.ArgumentParser()
parser.add_argument('-s', type=int, default=0)
parser.add_argument('-n', type=int, default=5, help='number of data files', dest='n')
parser.add_argument("-o", default=None, dest='o')


if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n
    s = args.s

    # solutions_iter = []
    # solutions_reviter = []
    solutions = []
    times = []

    for i in range(s, n+1):
        mat = np.load("data/cutMatrix{}.npy".format(i)).astype(int)
        d = json.load(open("data/cutMatrix{}.json".format(i)))["d"]
        # d = int(re.findall(r"d=(\d+)",
                # open("data/cutMatrix{}.py".format(i)).read())[0])
        # solutions_iter.append(IterativeSolver(mat, d).solve())
        # solutions_reviter.append(ReverseIterativeSolver(mat, d).solve())
        start_time = datetime.now()
        _is = IterativeSolver(mat, d).solve()
        ris = ReverseIterativeSolver(mat, d).solve()
        end_time = datetime.now()
        times.append((end_time - start_time).total_seconds())
        solutions.append(min([_is, ris], key=lambda x:x['metric']))


    # solutions_final = [min([si, ri], key=lambda x: x['metric'])
            # for si, sr in zip(solutions_iter, solutions_reviter)]

    # for s in solutions_final:
        # print(s)
    for i in solutions:
        # print(solutions_iter[i])
        # print(solutions_reviter[i])
        print(i)

    if args.o:
        with open(args.o + ".res", "w") as file:
            file.writelines(['{}, {}\n'.format(i, j['metric']) for i, j in enumerate(solutions, start=args.s)])

        with open(args.o + ".time", "w") as file:
            file.writelines(['{}, {}\n'.format(i, j) for i, j in enumerate(times, start=args.s)])

    # matrix = generate_random_matrix(n)
    # n = cutMatrix.d
    # matrix = check_and_prepare_matrix(np.matrix(cutMatrix.mat))
    # matrix = np.ones((n, n)) - np.eye(n)
    # matrix = np.matrix([[0, 1, 0, 0, 0],
                        # [1, 0, 1, 1, 0],
                        # [0, 1, 0, 1, 0],
                        # [0, 1, 1, 0, 1],
                        # [0, 0, 0, 1, 0]])
    # solutions_bf = [BruteForceSolver(matrix, i).solve() for i in range(1, n-1)]
    # solutions_iter = [IterativeSolver(matrix, i).solve() for i in range(1, n-1)]
    # solutions_reviter = [ReverseIterativeSolver(matrix, i).solve() for i in range(1, n-1)]

    # solutions_bf = [BruteForceSolver(matrix, n).solve()]

    # print(matrix)

    # solutions = {
            # # 'bf:' : solutions_bf,
            # 'iter: ': solutions_iter,
            # 'rev iter: ': solutions_reviter
            # }

    # for i in range(n-2):
        # print '='*10, i, '='*10
        # for solution_name in solutions:
            # print(solution_name)
            # print(solutions[solution_name][i])
            # print('-'*20)

