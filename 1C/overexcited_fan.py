t = int(input())

for test in range(t):
    x, y, string = input().split()
    x, y = int(x), int(y)
    ans = 'IMPOSSIBLE'
    nth_minute = 1
    for i in string:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'E':
            x += 1
        elif i == 'W':
            x -= 1
        if abs(x)+abs(y) <= nth_minute:
            # possible
            ans = nth_minute
            break
        
        nth_minute += 1

    print("Case #{}: {}".format(test+1, ans))
