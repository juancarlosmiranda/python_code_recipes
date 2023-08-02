"""
Author: Juan Carlos Miranda
Description:
    This program launch threads using Python. The code was developed implementing the OBJECT ORIENTED PROGRAMMING.
    This runs a text user interface in order to show the execution. It is based on curses
    pip courses.

Usage:
    python ui_main_thread_01.py
"""

"""
Run a UI with options for launch threads
python ui_main_thread_01.py
"""

import curses
import logging
import signal

from job_thread import JobThread

X_MESSAGE = 1
Y_MESSAGE = 1


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Service Exit --> \r')
    pass


def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServiceExit



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    my_screen = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)

    try:
        j1 = JobThread()
        # main loop
        key_pressed = None
        while key_pressed != ord('q'):
            my_screen.clear()
            my_screen.border(0)
            my_screen.addstr(2, 4, "MENU - Launch threads", curses.color_pair(3))
            my_screen.addstr(3, 4, "1 - Launch thread")
            my_screen.addstr(4, 4, "2 - Stopping thread")
            my_screen.addstr(8, 4, "q - Quit \n ")

            key_pressed = my_screen.getch()

            if key_pressed == ord('1'):
                if not j1.is_alive():
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> Launching thread!")
                    my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                    key_pressed = my_screen.getch()
                    my_screen.clear()
                    j1 = JobThread()
                    j1.start()
                else:
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> WE CAN'T START JOB, it is ALIVE()")
                    my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                    key_pressed = my_screen.getch()

            if key_pressed == ord('2'):
                if j1.is_alive():
                    j1.shutdown_flag.set()
                    j1.join()
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, 'UI -> STOPPING thread #%s ' % j1.ident)
                else:
                    my_screen.clear()
                    my_screen.addstr(X_MESSAGE, Y_MESSAGE, "UI -> We CAN'T STOP JOB, it is NOT ALIVE()")

                my_screen.addstr(X_MESSAGE + 2, Y_MESSAGE, 'UI -> Press any key!!')
                key_pressed = my_screen.getch()


            if key_pressed == ord('q'):
                if j1.is_alive():
                    j1.shutdown_flag.set()
                    j1.join()


        curses.endwin()


    except ServiceExit:
        print('ServiceExit Exception --> \r')
        print('CATCHING any Exception HERE!--> \r')
        j1.shutdown_flag.set()
        j1.join()
