import re

def convert_dat_to_py(path="cutMatrix.dat"):
    with open(path) as file:
        content = file.read()

    import ipdb; ipdb.set_trace()
    content_py, _ = re.subn(r"/[*].*[*]/", "", content)

    with open(path[:-3]+ "py", "w") as file:
        file.write(content_py)


def check_and_prepare_matrix(matrix):
    n = matrix.shape[0]
    for i in range(n):
        matrix[i, i] = 0
    return matrix

