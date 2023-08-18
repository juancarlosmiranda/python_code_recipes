"""
Project:
Author:
Date:
Description:

pip install windows-curses


Use:
"""
import curses

if __name__ == '__main__':
    myscreen = curses.initscr()
    height, width = myscreen.getmaxyx()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
    myscreen.border(0)

    x = None
    while x != ord('q'):
        myscreen.clear()
        myscreen.border(0)
        myscreen.addstr(2, 2, "Enter an option number...")
        myscreen.addstr(4, 4, "1 - Record 1080p ")
        myscreen.addstr(5, 4, "2 - Record 3072p")
        myscreen.addstr(6, 4, "3 - Test capture")
        myscreen.addstr(7, 4, "4 - Configure...")
        myscreen.addstr(8, 4, "q - Exit")

        myscreen.refresh()
        x = myscreen.getch()

        if x == ord('1'):
            myscreen.clear()
            myscreen.addstr(10, 10, "EXECUTING COMMAND -> 1")
            k = myscreen.getch()
            curses.endwin()

        if x == ord('2'):
            myscreen.clear()
            myscreen.addstr(10, 10, "EXECUTING COMMAND -> 2", curses.color_pair(1))
            myscreen.refresh()
            k = myscreen.getch()
            curses.endwin()

        if x == ord('3'):
            myscreen.clear()
            myscreen.addstr(10, 10, "EXECUTING COMMAND -> 3")
            k = myscreen.getch()
            curses.endwin()

        if x == ord('4'):
            myscreen.clear()
            myscreen.addstr(10, 10, "EXECUTING COMMAND -> 4")
            k = myscreen.getch()
            curses.endwin()

    curses.endwin()
