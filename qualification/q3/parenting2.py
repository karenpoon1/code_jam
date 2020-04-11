def same_person(string):
    string += string[-1]
    return string

def diff_person(string):
    if string[-1] == 'C':
        string += 'J'
    else:
        string += 'C'
    return string

def read_file():
    no_of_test = int(input())
    activity_cases = []
    numbers = []
    for case in range(no_of_test):
        no_of_activity = int(input())
        numbers.append(no_of_activity)
        times = []
        for i in range(no_of_activity):
            act_time = list(input().split())
            act_time = [int(i) for i in act_time]
            times.append(act_time)
        activity_cases.append(times)
    return no_of_test, activity_cases, numbers

no_of_test, activity_cases, numbers = read_file()

def algorithm(no_of_test, activity_cases, numbers):

    for i in range(no_of_test):
        string = 'C'
        orig_current_case = [[v, k] for v, k in enumerate(activity_cases[i])]
        current_case = sorted(orig_current_case, key = lambda x: x[1])
        key_list = [i[0] for i in current_case]
        current_case = [i[1] for i in current_case]
        number_of_activities = numbers[i]

        c_start, c_end = map(int, current_case[0])
        next_start, next_end = map(int, current_case[1])

        if next_start >= c_end:
            c_start, c_end = next_start, next_end
            j_start, j_end = 0, 0
            string = same_person(string)
        else:
            j_start, j_end = next_start, next_end
            string = diff_person(string)

        impossible = False

        for j in range(numbers[i]-2):
            start, end = map(int, current_case[j+2])

            if start >= c_end and start >= j_end:
                string = same_person(string)
                if list(string)[-1] == 'C':
                    c_end = end
                else: 
                    j_end = end

            elif start < c_end and start < j_end:
                impossible = True
                # continue

            elif start < c_end and start >= j_end:
                # j needs to finish, j can start new!, c_end unchanged
                string += 'J'
                j_end = end
                
            elif start >= c_end and start < j_end:
                # c needs to finish, c can start new!, j_end unchanged
                string += 'C'
                c_end = end

        if impossible:
            string = 'IMPOSSIBLE'
        else:
            string = string
            string_list = list(string)
            string = [x for _,x in sorted(zip(key_list,string_list))]
            string = ''.join(string)
        print("Case #{}: {}".format(i+1, string))
            
algorithm(no_of_test, activity_cases, numbers)
