import curses
from curses.textpad import rectangle

upper, left, lower, right = 0, 0, 0, 0

def initialize(height, width):
    global upper, left, lower, right

    upper, left, lower, right = int(height/2-10), int(width/2-10), int(height/2+10), int(width/2+10)
    # 8, 55, 28, 75

def draw_grid(stdscr, grid):
    rectangle(stdscr, upper-1, left-1, lower+1, right+1)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                stdscr.addstr(upper+row, left+col*2, "  ")
            elif grid[row][col] == 1:
                curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_CYAN)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 2:
                curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 3:
                curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 4:
                curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 5:
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 6:
                curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))
            elif grid[row][col] == 7:
                curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
                stdscr.addstr(upper+row, left+col*2, "  ", curses.color_pair(1))

def draw_bank(stdscr):
    rectangle(stdscr, upper, left-15, upper+5, left-5)
    stdscr.addstr(upper, left-12, "BANCO")

def draw_next(stdscr):
    rectangle(stdscr, upper, right+5, upper+5, right+15)
    stdscr.addstr(upper, right+9, "NXT")

def draw_queue(stdscr):
    rectangle(stdscr, upper+7, right+5, lower, right+15)
    stdscr.addstr(upper+7, right+8, "QUEUE")

#def draw_I(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_CYAN)
#
#    if orientation == "default":
#        stdscr.addstr(y-1, x-4, "        ", curses.color_pair(1))
#    elif orientation == "right":
#        for _y in range(y-2, y+2):
#            stdscr.addstr(_y, x, "  ", curses.color_pair(1))
#    elif orientation == "flipped":
#        stdscr.addstr(y, x-4, "        ", curses.color_pair(1))
#    elif orientation == "left":
#        for _y in range(y-2, y+2):
#            stdscr.addstr(_y, x-2, "  ", curses.color_pair(1))
#
#def draw_O(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
#    stdscr.addstr(9, 56, "    ", curses.color_pair(1))
#    stdscr.addstr(10, 56, "    ", curses.color_pair(1))
#
#def draw_T(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
#    stdscr.addstr(9, 56, "      ", curses.color_pair(1))
#    stdscr.addstr(10, 58, "  ", curses.color_pair(1))
#
#def draw_S(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
#    stdscr.addstr(9, 58, "    ", curses.color_pair(1))
#    stdscr.addstr(10, 56, "    ", curses.color_pair(1))
#
#def draw_Z(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
#    stdscr.addstr(9, 56, "    ", curses.color_pair(1))
#    stdscr.addstr(10, 58, "    ", curses.color_pair(1))
#
#def draw_J(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
#    stdscr.addstr(9, 56, "  ", curses.color_pair(1))
#    stdscr.addstr(10, 56, "      ", curses.color_pair(1))
#
#def draw_L(stdscr, orientation, x, y):
#    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
#    stdscr.addstr(9, 60, "  ", curses.color_pair(1))
#    stdscr.addstr(10, 56, "      ", curses.color_pair(1))
#
#def erase(stdscr, block):
#    x = block.x
#    y = block.y
#    orientation = block.orientation
#
#    if orientation == "default":
#        stdscr.addstr(y-1, x-4, "        ")
#    elif orientation == "right":
#        for _y in range(y-2, y+2):
#            stdscr.addstr(_y, x, "  ")
#    elif orientation == "flipped":
#        stdscr.addstr(y, x-4, "        ")
#    elif orientation == "left":
#        for _y in range(y-2, y+2):
#            stdscr.addstr(_y, x-2, "  ")
