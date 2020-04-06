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
print(is_anti_revcomp(array))

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

    counter = 0

    for i in range(b/2):

        print(i+1)
        array[i] = input()
        print(b-i)
        array[-(i+1)] = input()

        if not random_pattern:
            mirrored = is_anti_reverse(array)
            anti_mirrored = is_anti_revcomp(array)
            if not mirrored and not anti_mirrored:
                random_pattern = True
      
        
      

        



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
