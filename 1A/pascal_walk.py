t = int(input())

for test_no in range(t):
    integer = int(input())
    integer_copy = 0
    i = 0
    while integer_copy <= integer:
        integer_copy += 2**i
        i += 1
    i -= 1
    integer_copy -= 2**i
    no_ones = integer - integer_copy
    step_list = []
    j = 0
    for row_no in range(i):
        row_list = []
        for element_no in range(row_no+1):
            row_list.append((row_no+1,element_no+1))
        if (row_no+1)%2 == 1:
            row_list = row_list[::-1]
        step_list.extend(row_list)
    if no_ones != 0:
        for j in range(no_ones):
            if i%2 == 1: # odd number
                step_list.append((i+1+j, 1))
            else:
                step_list.append((i+1+j, i+1+j))
    print("Case #{}:".format(test_no+1))
    for position in step_list:
        print(position[0], position[1])
    print(len(step_list))
