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
    # occupance can only be 0 or 1 or 2
    occupance = 0
    for i in range(no_of_test):
        string = 'C'
        orig_current_case = {v: k for v, k in enumerate(activity_cases[i])}
        current_case = dict(sorted(orig_current_case.items(), key=lambda v:v[1]))
        key_list = list(current_case.keys())
        current_case = list(current_case.values())
        number_of_activities = numbers[i]
        most_end = 0

        for j in range(numbers[i]-1):
            curr_start, curr_end = map(int, current_case[j])
            next_start, next_end = map(int, current_case[j+1])

            if next_start >= curr_end:
                occupance += 0
                string = same_person(string)


                if i != 0 and next_end > most_end:
                    most_end = next_end
                    occupance -= 1

            else: # if next_start < curr_end:
                occupance += 1
                if occupance > 1:
                    continue
                string = diff_person(string)
                if i == 0:
                    end1 = curr_end
                    end2 = next_end


                # if next_end < curr_end: # within
                #     most_end = curr_end
                # else:
                #     most_end = next_end














                string = same_person(string)
                if i != 0:
                    if curr_start < most_end:
                        occupance += 0
                    else: # if curr_start >= most_end:
                        occupance -= 1
            else: # if next_start < curr_end:
                occupance += 1
                string = diff_person(string)
                if occupance > 1:
                    continue
                if next_end < curr_end:
                    most_end = next_end
                else:
                    most_end = curr_end

        if occupance > 1:
            string = 'IMPOSSIBLE'
        else:
            string_list = list(string)
            string = [x for _,x in sorted(zip(key_list,string_list))]
            string = ''.join(string)
        print("Case #{}: {}".format(i+1, string))
            
algorithm(no_of_test, activity_cases, numbers)

"""
       for j in range(numbers[i]-1):
            curr_start, curr_end = map(int, current_case[j])
            next_start, next_end = map(int, current_case[j+1])

            if i==0 and next_start >= curr_end:
                occupance += 0
                string = same_person(string)
                c_end = next_end if list(string)[-1] == 'C' else j_end = next_end
            else: # if next_start < curr_end:
                occupance += 1
                string = diff_person(string)
                c_end = curr_end and j_end = next_end if list(string)[-1] == 'C' else j_end = curr_end and c_end = next_end

            if i != 0:
                if next_start > c_end and next_start > j_end:
                    string = same_person(string)
                    c_end = next_end if list(string)[-1] == 'C' else j_end = next_end

                if next_start < c_end and next_start < j_end:
                    impossible = True

                if next_start < c_end and next_start > j_end:
                    # j needs to finish, j can start new!, c_end unchanged
                    string = same_person(string)
                    j_end = next_end
                    
                if next_start > c_end and next_start < j_end:
                    # c needs to finish, c can start new!, j_end unchanged
                    string = same_person(string)
                    c_end = next_end

                

                # if next_end < curr_end: # within
                #     most_end = curr_end
                # else:
                #     most_end = next_end
"""