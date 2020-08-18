from Game import Game
from curses import wrapper
import curses
import Graphics 
import threading
import time

game = Game()

def key_listener(stdscr):
    while game.gameover == False:
        c = stdscr.getch()
        curses.flushinp()

        if c == curses.KEY_UP:
            game.rotate_block(stdscr, game.current_block) 
        elif c == curses.KEY_DOWN:
            game.move_block(stdscr, game.current_block, "down")
        elif c == curses.KEY_LEFT:
            game.move_block(stdscr, game.current_block, "left")
        elif c == curses.KEY_RIGHT:
            game.move_block(stdscr, game.current_block, "right")
        elif c == ord(" "):
            game.move_block(stdscr, game.current_block, "bottom")
        elif c == ord("q"):
            game.gameover = False
        time.sleep(0.05)

def main(stdscr):
    curses.initscr()
    stdscr.clear()

    game.start()
    Graphics.initialize(stdscr, height=curses.LINES-1, width=curses.COLS-1)
    Graphics.draw_queue(stdscr)
    Graphics.draw_bank(stdscr)
    Graphics.draw_next(stdscr)
    Graphics.draw_grid(stdscr, game.grid)

    t = threading.Thread(name ='daemon', target=key_listener, args=(stdscr,))
    t.setDaemon(True)
    t.start()

    while game.gameover == False:
        game.move_block(stdscr, game.current_block, "down")

        stdscr.refresh()
        time.sleep(1)

wrapper(main)
