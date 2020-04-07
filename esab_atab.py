def reverse(array):
    return array[::-1]

def complement(array):
    return [int(not i) if i != None else None for i in array ]

def rev_comp(array):
    return complement(reverse(array))

def remove_none(array):
    return [value for value in array if value != None]

def is_anti_reverse(array):
    array = remove_none(array)
    return array == reverse(array)

def is_anti_revcomp(array):
    array = remove_none(array)
    return array == rev_comp(array)

# array = [1,0,0,None,None,None,None,0,0,1] #anti_reverse (reverse = nothing, complement = rev_comp)
# array = [1,0,0,1,None,None,0,1,1,0] #anti_revcomp (reverse = complement, rev_comp = nothing)
# array = [1,1,None, None, 1,1]
# print(complement(array))

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
        # print(array)
        # print("query counter: ", query_counter, query_counter % 10)

        print(b-i)
        query_counter += 1
        array[-(i+1)] = int(input())
        # print(array)
        # print("query counter: ", query_counter, query_counter % 10)

        i += 1
        checked_until = i
        # print("checked until:", checked_until)
        # print("query counter", query_counter)

        if not None in array:
            # got everything, submit answer!
            string = ''.join([str(i) for i in array])
            print(string)
            break

        if not random_pattern:
            mirrored = is_anti_reverse(array)
            anti_mirrored = is_anti_revcomp(array)
            if not mirrored and not anti_mirrored:
                random_pattern = True
                random_start_pos = i - 1

        if query_counter % 10 == 0: # random quantisation
            # print("query counter: ", query_counter)
            if random_pattern:
                # check random_start_pos and the one before
                j = random_start_pos
                new_array = [array[j-1], array[j], array[-(j+1)], array[-j]]
                # print("newarray", new_array)

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
