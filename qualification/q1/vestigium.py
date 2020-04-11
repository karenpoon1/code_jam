import numpy as np

def read_file():
    filename = 'input_files/input.txt'

    with open(filename, 'r') as f:
        no_of_test = int(f.readline())
        matrices = []
        sizes = []
        for case_i in range(no_of_test):
            size_n = int(f.readline())
            sizes.append(size_n)
            matrix = []
            for row_i in range(size_n):
                row = list(f.readline().split())
                matrix.append(row)
            matrices.append(np.array(matrix))
    return no_of_test, sizes, matrices


def write_file(output):
    filename = 'output.txt'
    with open(filename, 'w') as f:
        for line in output:
            f.write(str(line) + '\n')


def algorithm(no_of_test, matrix_sizes, matrices):
    output = []
    for i in range(no_of_test):
        trace = 0
        row_dup = 0
        column_dup = 0
        for n in range(matrix_sizes[i]):
            trace += int(matrices[i][n][n])
        # print(matrices[i])
        for row in matrices[i]:
            if len(set(row)) != len(list(row)):
                # there is duplicates
                row_dup += 1
        for column in matrices[i].transpose():
            if len(set(column)) != len(list(column)):
                # there is duplicates
                column_dup += 1            

        output.append(f"Case #{i+1}: {trace} {row_dup} {column_dup}")

    write_file(output)


if __name__ == "__main__":
    no_of_test, matrix_sizes, matrices = read_file()
    algorithm(no_of_test, matrix_sizes, matrices)
