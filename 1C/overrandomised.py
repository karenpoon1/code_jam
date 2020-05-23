t = int(input())

for test in range(t):
    U = int(input())
    max_range = 10**U
    string = ''
    line_number = 0
    digit_number = [1]
    while line_number < 10000:
        M_str, R_str = input().split()
        M_int = int(M_str)
        if len(R_str) == len(M_str):
            if int(M_str[0]) == digit_number and string == '':
                string += R_str[0]
                digit_number += 1

            if int(M_str[0]) == digit_number:
                if R_str[0] not in string:
                    string += R_str[0]
            elif int(M_str[1]) == digit_number and int(M_str[0]) < int(M_str[1]):
                if R_str[1] not in string:


            int(M_str[0]) == digit_number and string[0] != M_str[0]:
                string += R_str[0]

                

        if len(R_str) > len(M_str): # can be any digit
            pass
        elif len(R_str) == len(M_str):
            # R_str[0] 
            posssibility = [i+1 for i in range(int(M_str[0]))]

            
        line_number += 1