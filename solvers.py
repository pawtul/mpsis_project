from itertools import combinations

import numpy as np


class Infinity(object):
    def __cmp__(self, other):
        return 1


class BaseSolver(object):
    def __init__(self, matrix, number_to_remove):
        self.matrix = matrix
        self.number_to_remove = number_to_remove
        self.matrix_size = matrix.shape[0]

    def get_metric(self, sets):
        return sum(len(i)*(len(i) - 1) / 2. for i in sets)

    def exclude_nodes(self, nodes):
        matrix = np.matrix(self.matrix)
        for node in nodes:
            matrix[node, :] = [0] * self.matrix_size
            matrix[:, node] = [[0]] * self.matrix_size
        return matrix

    def group_neighbours(self, matrix):
        sets = []
        for node_index in range(self.matrix_size - 1):
            for s in sets:
                if node_index in s:
                    break
            else:
                s = {node_index}
                sets.append(s)
            s.update([i for i in range(self.matrix_size) if matrix[node_index, i]])
        return sets

    def check_metric_with_excluded_nodes(self, excluded_nodes):
        matrix = self.exclude_nodes(excluded_nodes)
        sets = self.group_neighbours(matrix)
        return self.get_metric(sets)

    def solve(self):
        return None


class BruteForceSolver(BaseSolver):
    def solve(self):
        best_combination = None
        for nodes in combinations(range(self.matrix_size), self.number_to_remove):
            metric = self.check_metric_with_excluded_nodes(nodes)
            if not best_combination:
                best_combination = {"nodes": nodes, "metric":metric}
            if metric < best_combination["metric"]:
                best_combination = {"nodes": nodes, "metric":metric}
        return best_combination


class IterativeSolver(BaseSolver):
    def solve(self):
        node_numbers = range(self.matrix_size)
        best_combination = {'nodes': set(), 'metric': Infinity()}
        while len(best_combination) < self.number_to_remove:
            for node in node_numbers:
                new_metric = self.check_metric_with_excluded_nodes(
                        list(best_combination['nodes']) + [node])

                if new_metric <= best_combination['metric']:
                    best_combination['nodes'].add(node)

                best_combination['metric'] = min(
                        best_combination['metric'], new_metric)
        return best_combination

