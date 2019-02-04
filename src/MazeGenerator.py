# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB36 - 20130106
import random


def generate_maze(mx, my, cx, cy):
    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1];
    dy = [-1, 0, 1, 0]  # 4 directions to move in the maze
    maze[cy][cx] = 1;
    stack = [(cx, cy, 0)]  # stack element: (x, y, direction)
    good_points = []

    while len(stack) > 0:
        (cx, cy, cd) = stack[-1]
        # to prevent zigzags:
        # if changed direction in the last move then cannot change again
        if len(stack) > 2:
            if cd != stack[-2][2]:
                dirRange = [cd]
            else:
                dirRange = range(4)
        else:
            dirRange = range(4)

        # find a new cell to add
        nlst = []  # list of available neighbors
        for i in dirRange:
            nx = cx + dx[i];
            ny = cy + dy[i]
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if maze[ny][nx] == 0:
                    ctr = 0  # of occupied neighbors must be 1
                    for j in range(4):
                        ex = nx + dx[j];
                        ey = ny + dy[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1: ctr += 1
                    if ctr == 1: nlst.append(i)

        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            cx += dx[ir];
            cy += dy[ir];
            maze[cy][cx] = 1
            good_points.append((cx, cy))
            stack.append((cx, cy, ir))
        else:
            stack.pop()
    return maze, good_points[len(good_points) // 2]
