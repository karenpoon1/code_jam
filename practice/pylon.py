import random

t = int(input())

for i in range(t):
    r, c = map(int, input().split())
    size = (r, c)
    # impossible cases: 2x2, 2x3, 2x4, 3x3
    impossible_cases = [(2,2), (2,3), (2,4), (3,2), (3,3), (4,2)]
    if size in impossible_cases:
        print("Case #{}: IMPOSSIBLE".format(i+1))
    else:
        print("Case #{}: POSSIBLE".format(i+1))
        while True:    
            grid = [(x+1, y+1) for x in range(r) for y in range(c)]
            temp_grid = grid.copy()
            new_grid = []
            start_pos = random.choice(grid)
            prev_r, prev_c = start_pos

            grid.remove(start_pos)
            new_grid.append(start_pos)

            while len(temp_grid) != 0:
                new_pos = random.choice(temp_grid)
                new_r, new_c = new_pos

                temp_grid.remove(new_pos)

                if new_r != prev_r and new_c != prev_c and abs(new_r - new_c) != abs(prev_r - prev_c) and new_r + new_c != prev_r + prev_c:
                    grid.remove(new_pos)
                    new_grid.append(new_pos)
                    prev_r, prev_c = new_r, new_c
                    temp_grid = grid.copy()

            if len(grid) == 0:
                break

        for i in new_grid:
            print(i[0], i[1])
