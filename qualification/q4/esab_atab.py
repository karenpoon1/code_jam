def reverse(array):
    return array[::-1]

def complement(array):
    return [int(not i) if i != None else None for i in array ]

def rev_comp(array):
    return complement(reverse(array))

def remove_none(array):
    return [value for value in array if value != None]

def anti_reverse(array):
    array = remove_none(array)
    return array == reverse(array)

def anti_revcomp(array):
    array = remove_none(array)
    return array == rev_comp(array)

t, b = map(int, input().split())

for test_case in range(t):
    array = [None] * b

    mirrored = None 
    anti_mirrored = None
    random_pattern = None

    query_counter = 0
    i = 0

    while query_counter < 150:

        print(i+1)
        query_counter += 1
        array[i] = int(input())

        print(b-i)
        query_counter += 1
        array[-(i+1)] = int(input())

        i += 1
        checked_until = i

        if not None in array:
            # got everything, submit answer!
            string = ''.join([str(i) for i in array])
            print(string)
            break

        if not random_pattern:
            if not anti_reverse(array) and not anti_revcomp(array):
                random_pattern = True
                random_start_pos = i - 1

        if query_counter % 10 == 0: # random fluctuation
            if random_pattern:
                # check random_start_pos and the one before
                j = random_start_pos
                new_array = [array[j-1], array[j], array[-(j+1)], array[-j]]

                print(random_start_pos)
                query_counter += 1
                check1 = int(input())

                print(random_start_pos+1)
                query_counter += 1
                check2 = int(input())

                if check1 == new_array[0] and check2 == new_array[1]:
                    # nothing
                    pass
                elif check1 == new_array[-1] and check2 == new_array[-2]:
                    # reversed
                    array = reverse(array)
                elif check1 != new_array[0] and check2 != new_array[1]:
                    # complemented
                    array = complement(array)
                else:
                    # rev and comp
                    array = rev_comp(array)
                # print("after quantisation", array)
            
            else: # anti_mirrored

                print(checked_until)
                query_counter += 1
                check1 = int(input())

                print(b-checked_until+1)
                query_counter += 1
                check2 = int(input())

                if check1 == array[checked_until-1]:
                    pass
                else:
                    array = complement(array)
    
    response = str(input())
    if response == 'N':
        print("wrong")
        break
