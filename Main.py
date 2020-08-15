from Game import Game
from curses import wrapper
import curses
import Graphics 

game = Game()

def main(stdscr):
    # initial set-up
    c = stdscr.getch()

    while True:
        if c == 10: # enter key
            game.start()
            Graphics.initialize(height=curses.LINES-1, width=curses.COLS-1)
            Graphics.draw_queue(stdscr)
            Graphics.draw_bank(stdscr)
            Graphics.draw_next(stdscr)
            Graphics.draw_grid(stdscr, game.grid)
            break

    while game.gameover == False:
        Graphics.draw_block(stdscr, game.current_block)

        c = stdscr.getch()

        if c == curses.KEY_UP:
            game.current_block.rotate() 
        elif c == curses.KEY_DOWN:
            Graphics.erase(stdscr, game.current_block)
            game.current_block.move("down") 
        elif c == curses.KEY_LEFT:
            Graphics.erase(stdscr, game.current_block)
            game.current_block.move("left") 
        elif c == curses.KEY_RIGHT:
            Graphics.erase(stdscr, game.current_block)
            game.current_block.move("right") 
        elif c == ord("q"):
            break
        else:
            continue


wrapper(main)
