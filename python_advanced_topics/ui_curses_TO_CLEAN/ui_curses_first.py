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
    myscreen.border(0)
    myscreen.addstr(12, 25, "A first example using Curses in Python!")
    myscreen.refresh()
    myscreen.getch()
    curses.endwin()





