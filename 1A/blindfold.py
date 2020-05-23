t, a, b = map(int, input().split())

for test_case in range(t):
    radius = a
    left_wall_size = 1e9
    leeway = left_wall_size - radius
    
    tries = 0
    i = 0
    y = 0

    vertical_centre = False
    horizontal_centre = False
    circle_above_centre = None
    first_hit = False

    while tries < 300:

        print(-left_wall_size+i, y)
        tries += 1
        result = input()

        if result == 'HIT':
            first_hit = True
            if tries == 0:
                # circle is vertically centered
                vertical_centre = True
                continue
            else:
                mark = -left_wall_size+i
                if first_hit:
                    y += 1 # if circle above centre
                else:
                    y -= 1

        elif result == 'MISS':
            if not first_hit:
                distance_from_centre = y-1
                continue

            elif first_hit:
                # circle is below centre
                circle_above_centre = False
                first_hit = False
                y = 0

            else:
                i += 1


    while tries < 300:
        

