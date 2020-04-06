def reverse(array):
    return array[::-1]

def complement(array):
    return [int(not i) for i in array]

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


array = [1,0,0,None,None,None,None,0,0,1] #anti_reverse (reverse = nothing, complement = rev_comp)
array = [1,0,0,1,None,None,0,1,1,0] #anti_revcomp (reverse = complement, rev_comp = nothing)
array = [1,1,1,1]
if not None in array:
    print(array)

t, b = map(int, input().split())

for test_case in range(t):
    array = [None] * b

    reverse = False
    complement = False
    rev_comp = False
    nothing = False

    mirrored = None 
    anti_mirrored = None
    random_pattern = None

    query_counter = 0
    i = 0
    while query_counter < 150:

        print(i+1)
        query_counter += 1
        array[i] = input()

        print(b-i)
        query_counter += 1
        array[-(i+1)] = input()

        i += 1

        if not random_pattern:
            mirrored = is_anti_reverse(array)
            anti_mirrored = is_anti_revcomp(array)
            if not mirrored and not anti_mirrored:
                random_pattern = True
                random_start_pos = i

        if query_counter != 1 and query_counter % 10 == 1: #random quantisation
            if random_pattern:
                # check random_start_pos and the one before
                new_array = [array[i-1], array[i], array[-(i+1)], array[-i]]

                print(random_start_pos)
                query_counter += 1
                check1 = input()

                print(random_start_pos-1)
                query_counter += 1
                check2 = input()

                if check1 == new_array[0] and check2 == new_array[1]:
                    nothing = True
                elif check1 == new_array[-1] and check2 == new_array[-2]:
                    reverse = True
                    array = reverse(array)
                elif check1 != new_array[0] and check2 != new_array[1]:
                    complement = True
                    array = complement(array)
                else:
                    rev_comp = True
                    array = rev_comp(array)
            
            elif mirrored:
                


        if not None in array:
            # got everything, submit answer!
            print(array)

                

                
        reverse = False
        complement = False
        rev_comp = False
        nothing = False



        if i == b/2:
            i = 0
        

        



#         if i < 5:
#             print(i+1)
#             array[i] = input()
#         else:
#             print(-(b-i))
#             array[-(b-i)] = input()

#     # check mirror
#     if array[:5] == reverse(array[-5:])
#         mirror = True # this section of array is immune to reverse
    
#     if array[:5] == complement(array[-5:])
#         anti_mirror = True # this section of array is immune to complement
    
#     if array[:5] == rev_comp(array[-5:])
#         anti_revcomp = True # this section of array is immune to rev_comp
