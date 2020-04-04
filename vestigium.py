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
                row = f.readline().split()
                row = list(row)
                matrix.append(row)
            matrices.append(matrix)
    return no_of_test, sizes, matrices

def algorithm(no_of_test, matrix_sizes, matrices):
    for i in range(no_of_test):
        



if __name__ == "__main__":
    no_test, matrix_sizes, matrices = read_file()
