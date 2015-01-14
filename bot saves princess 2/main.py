#!/bin/python
def nextMove(n,r,c,grid):
    for p_r in range(len(grid)):
        # Get Princess position
        p_c = grid[p_r].find('p')
        if p_c > -1:
            bot = [p_r, p_c]

    r_diff = r - bot[0]
    c_diff = c - bot[1]

    if r_diff > 0:
        for k in range(abs(r_diff)):
            return 'UP'
    else:
        for k in range(abs(r_diff)):
            return 'DOWN'

    if c_diff > 0:
        for k in range(abs(c_diff)):
            return 'LEFT'
    else:
        for k in range(abs(c_diff)):
            return 'RIGHT'

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)