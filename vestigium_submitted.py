import numpy as np

def read_file():

    no_of_test = int(input())
    matrices = []
    sizes = []
    for case_i in range(no_of_test):
        size_n = int(input())
        sizes.append(size_n)
        matrix = []
        for row_i in range(size_n):
            row = list(input().split())
            matrix.append(row)
        matrices.append(np.array(matrix))
    return no_of_test, sizes, matrices


def algorithm(no_of_test, matrix_sizes, matrices):
    for i in range(no_of_test):
        trace = 0
        row_dup = 0
        column_dup = 0
        for n in range(matrix_sizes[i]):
            trace += int(matrices[i][n][n])
        for row in matrices[i]:
            if len(set(row)) != len(list(row)):
                row_dup += 1
        for column in matrices[i].transpose():
            if len(set(column)) != len(list(column)):
                column_dup += 1            

        print("Case #{}: {} {} {}".format(i+1, trace, row_dup, column_dup))


if __name__ == "__main__":
    no_of_test, matrix_sizes, matrices = read_file()
    algorithm(no_of_test, matrix_sizes, matrices)
