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
    string = 'C'
    c_available = False
    j_available = True
    for i in range(no_of_test):
        current_case = activity_cases[i]
        number_of_activities = numbers[i]
        if number_of_activities == 2:
            for j in range(numbers[i]-1):
                curr_start, curr_end = map(int, current_case[j])
                next_start, next_end = map(int, current_case[j+1])
                if next_start >= curr_end:
                    string = same_person(string)
                else:
                    string = diff_person(string)
            return string
        else:
            for j in range(numbers[i]-2):
                curr_start, curr_end = map(int, current_case[j])
                next_start, next_end = map(int, current_case[j+1])
                next2_start, next2_end = map(int, current_case[j+2])

                if next_start >= curr_end:
                    string = same_person(string)
                elif next_start < curr_end:
                    string = diff_person(string)
print(string)
            