#!/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    for r in range(len(grid)):
        # Get bot position
        c = grid[r].find('m')
        if c > -1:
            bot = [r, c]
        # Get princess position
        c = grid[r].find('p')
        if c > -1:
            princess = [r, c]

    r_diff = bot[0] - princess[0]
    c_diff = bot[1] - princess[1]

    if r_diff > 0:
        for k in range(abs(r_diff)):
            print 'UP'
    else:
        for k in range(abs(r_diff)):
            print 'DOWN'

    if c_diff > 0:
        for k in range(abs(c_diff)):
            print 'LEFT'
    else:
        for k in range(abs(c_diff)):
            print 'RIGHT'

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)

if __name__ == '__main__':
    pass