no_of_test = int(input())
for case in range(no_of_test):
    input_string = list(input())
    string = ''
    n = int(input_string[0])
    string += '(' * n + str(n)
    for i in range(len(input_string)-1):
        curr_digit = int(input_string[i])
        next_digit = int(input_string[i+1])
        if curr_digit == next_digit:
            string += str(next_digit)
        elif curr_digit > next_digit:
            diff = curr_digit - next_digit
            string += ')' * diff + str(next_digit)
        elif curr_digit < next_digit:
            diff = next_digit - curr_digit
            string += '(' * diff + str(next_digit)
    last_digit = int(input_string[-1])
    string += ')' * last_digit
    print("Case #{}: {}".format(case+1, string))
