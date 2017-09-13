# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    open = []
    used = []
    used.append([0, init[0], init[1]])

    expand = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    expand_counter = 0

    g_value = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    open.append([0, init[0], init[1]])
    while [open[0][1], open[0][2]] != goal:
        current_pos = open.pop(0)

        expand[current_pos[1]][current_pos[2]] = expand_counter
        expand_counter += 1

        g_value[current_pos[1]][current_pos[2]] = current_pos[0]

        for direction in delta:
            future_pos = [current_pos[0] + cost, current_pos[1] + direction[0], current_pos[2] + direction[1]]
            if 0 <= future_pos[1] < len(grid) and 0 <= future_pos[2] < len(grid[0]):  # Innerhalb des Grids?
                if grid[future_pos[1]][future_pos[2]] == 0:                           # Hindernis im Weg?
                    used_var = False
                    for i_used in used:
                        if [future_pos[1], future_pos[2]] == [i_used[1], i_used[2]]: # War Roboter da schon?
                            used_var = True
                    if not used_var:
                        future_pos[0] += heuristic[future_pos[1]][future_pos[2]]
                        open.append(future_pos)
                        used.append(future_pos)
        open = sorted(open, key=lambda x: x[0])
        if not open:

            for i in range(len(expand)):
                for n in range(len(expand[i])):
                    if expand[i][n] == 0:
                        expand[i][n] = -1
            expand[init[0]][init[1]] = 0

            return 'fail', expand, g_value

    for i in range(len(expand)):
        for n in range(len(expand[i])):
            if expand[i][n] == 0:
                expand[i][n] = -1
    expand[init[0]][init[1]] = 0
    expand[goal[0]][goal[1]] = expand_counter

    return open[0], expand, g_value


result, expand, g_value = search(grid, init, goal, cost)

print(result)

for i in expand:
    print(i)
