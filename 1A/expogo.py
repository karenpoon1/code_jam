def quad(string, quad_no):
    s = 'SENW'
    index = s.find(string)
    index += (quad_no-1)
    if index > 3:
        index -= 4
    return s[index]


def combine(string, quad_no):
    new_string = ''
    for character in string:
        new_string += quad(character, quad_no)
    return new_string


t = int(input())

for test_no in range(t):
    x, y = map(int, input().split())
    if abs(x)%2 == 0 and abs(y)%2 == 0:
        ans = 'IMPOSSIBLE'
    elif abs(x)%2 == 1 and abs(y)%2 == 1:
        ans = 'IMPOSSIBLE'
    elif x == 0 or y == 0:
        if x == 0:
            temp_int = abs(y)
        elif y == 0:
            temp_int = abs(x)
            
        if temp_int == 1:
            ans = 'E'
        elif temp_int == 2:
            ans = 'IMPOSSIBLE'
        elif temp_int == 3:
            ans = 'EE'
        elif temp_int == 4:
            ans = 'IMPOSSIBLE'
    
        if y == 0 and x > 0:
            quad_no = 1
        elif y == 0 and x < 0:
            quad_no = 3
        elif x == 0 and y > 0:
            quad_no = 2
        elif x == 0 and y < 0:
            quad_no = 4

    else: 
        if x > 0 and y > 0:
            quad_no = 1
        elif x < 0 and y > 0:
            quad_no = 2
            x, y = y, x
        elif x < 0 and y < 0:
            quad_no = 3
        elif x > 0 and y < 0:
            quad_no = 4
            x, y = y, x

        if abs(x) == 1:
            if abs(y) == 2:
                ans = 'EN'
            elif abs(y) == 4:
                ans = 'WEN'
        elif abs(x) == 2:
            if abs(y) == 1:
                ans = 'NE'
            elif abs(y) == 3:
                ans = 'SEN'
        elif abs(x) == 3:
            if abs(y) == 2:
                ans = 'WNE'
            elif abs(y) == 4:
                ans = 'EEN' 
        elif abs(x) == 4:
            if abs(y) == 1:
                ans = 'SNE'
            elif abs(y) == 3:
                ans = 'NNE'           


    if ans != 'IMPOSSIBLE':
        ans = combine(ans, quad_no)
    
    print("Case #{}: {}".format(test_no+1, ans))
