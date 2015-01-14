#!/usr/bin/python
def next_move(posr, posc, board):
    num_rows = 5
    if board[posr][posc] == 'd':
        print "CLEAN"
    else:
        row_parity = posr % 2
        if row_parity == 0:
            # Even row go right if there is still dirt in the current row, otherwise, go down
            row_has_dirt = False
            for k in range(posc + 1, num_rows):
                if board[posr][k] == 'd':
                    row_has_dirt = True
                    break
            if row_has_dirt:
                print "RIGHT"
            else:
                if posr < num_rows - 1:
                    next_row_has_dirt_ahead = False
                    for k in range(posc + 1, num_rows):
                        if board[posr + 1][k] == 'd':
                            next_row_has_dirt_ahead = True
                            break
                    if next_row_has_dirt_ahead:
                        print "RIGHT"
                    else:
                        print "DOWN"
                else:
                    print ""
        else:
            # Odd row go left if there is still dirt in the current row, otherwise, go down
            row_has_dirt = False
            for k in range(0, posc):
                if board[posr][k] == 'd':
                    row_has_dirt = True
                    break
            if row_has_dirt:
                print "LEFT"
            else:
                if posr < num_rows - 1:
                    next_row_has_dirt_ahead = False
                    for k in range(0, posc):
                        if board[posr + 1][k] == 'd':
                            next_row_has_dirt_ahead = True
                            break
                    if next_row_has_dirt_ahead:
                        print "LEFT"
                    else:
                        print "DOWN"
                else:
                    print ""

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
