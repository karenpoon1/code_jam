# def read_file():
#     filename = 'input_files/.txt'

#     with open(filename, 'r') as f:
#         no_test_case = int(f.readline())
#         number_1 = 

def two_numbers_without_four(N):
    N_string = list(str(N))
    for i in range(len(N_string)):
        if N_string[i] == '4':
            N_string[i] = '3'
    A = int(''.join(N_string))
    B = N - A
    return A, B

print(two_numbers_without_four(25464874531))
