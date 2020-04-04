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
            times.append(act_time)
        activity_cases.append(times)
    return no_of_test, activity_cases, numbers

no_of_test, activity_cases, numbers = read_file()

def algorithm(no_of_test, activity_cases, numbers):
    # occupance can only be 0 or 1 or 2
    occupance = 1
    for i in range(no_of_test):
        string = 'C'
        current_case = activity_cases[i]
        number_of_activities = numbers[i]
        for j in range(numbers[i]-1):
            curr_start, curr_end = map(int, current_case[j])
            next_start, next_end = map(int, current_case[j+1])
            if next_start >= curr_end:
                occupance -= 1
                # activity finishes, not occupied
                string = same_person(string)
            else:
                occupance += 1
                if occupance > 2:
                    string = 'IMPOSSIBLE'
                    continue
                string = diff_person(string)
                if next_end < curr_end:
                    occupance -= 1
                else:
                    occupance += 1
        if occupance > 2:
            string = 'IMPOSSIBLE'

        print("Case #{}: {}".format(i+1, string))
            
algorithm(no_of_test, activity_cases, numbers)
