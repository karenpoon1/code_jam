import re
t = int(input())

for test_case in range(t):
    n = int(input())
    string = input()

    for i in range(n-1):

        string_split = re.split('(\W*)', string)

        if string_split[0] != '*':
            start_fixed = True
        if string_split[-1] != '*':
            end_fixed = True
        if start_fixed and end_fixed and '*' not in string:
            middle_fixed = True

        pattern = input()
        pattern_split = re.split('(\W*)', pattern)
        
        if pattern_split[0] != '*':
            pattern_start_fixed = True
        if pattern_split[-1] != '*':
            pattern_end_fixed = True
        if start_fixed and end_fixed and '*' not in string:
            pattern_middle_fixed = True

        impossible = False

        if start_fixed and pattern_start_fixed:
            if string_split[0] not in pattern_split[0] and pattern_split[0] not in string_split[0]:
                impossible = True
                continue
        if end_fixed and pattern_end_fixed:
            if string_split[-1] not in pattern_split[-1] and pattern_split[-1] not in string_split[-1]:
                impossible = True
                continue
        



        if start_fixed and not end_fixed:
            if pattern_start_fixed:
                if string_split[0] in pattern_split[0]:
                    string_split[0] = pattern_split[0]
                elif pattern_split[0] in string_split[0]:
                    pass
                else: 
                    string = '*'
                    continue
            else:
                string_split.append(pattern_split[1:])
        
        elif end_fixed and not start_fixed:
            if pattern_end_fixed:
                if string_split[-1] in pattern_split[-1]:
                    string_split[-1] = pattern_split[-1]
                elif pattern_split[-1] in string_split[-1]:
                    pass
                else: 
                    string = '*'
                    continue
            else:
                string_split = pattern_split.append(string_split[1:])

        elif start_fixed and end_fixed:



                



            



    start_fixed = False
    end_fixed = False
    middle_fixed = False

    pattern = [input() for i in range(n)]
    string = '*'
    string_split = re.split('(\W*)', string)
    print(string)
    for i in pattern:
        if string[0] != *:
            start_fixed = True
        if string[-1] != *:
            end_fixed = True
        if start_fixed and end_fixed and '*' not in string:
            middle_fixed = True
        
        if pattern[i][0] == '*' and pattern[i][-1] == '*':
            # not fixed
            string.replace('*', pattern, 1)
        if pattern[i][0] == '*' and pattern[i][-1] != '*':
            # end fixed
            
            



    # for i in range(n-1):
    #     pattern = input()
    #     if pattern[0] != *:

    #         # start is fixed

    #     if pattern[-1] == *:
    #         # end is anything
    #     if pattern[0] != * and pattern[-1] != *
