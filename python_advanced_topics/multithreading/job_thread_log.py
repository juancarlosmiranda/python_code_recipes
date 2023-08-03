"""
Author: Juan Carlos Miranda
Description:
    Threading implementing as class with logging instructions

Usage:
    j1 = JobThreadLog()
    j1.start()

"""

import time
import threading
import logging

class JobThreadLog(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()

    def run(self):
        print('JobThreadLog STARTED #%s' % self.ident)
        logging.info('JobThreadLog STARTED #%s' % self.ident)

        # meanwhile is running
        while not self.shutdown_flag.is_set():
            print(f'JobThreadLog WORKING #{self.ident}')
            logging.info(f'JobThreadLog WORKING #{self.ident}')
            time.sleep(1)

        # ... Clean shutdown code here ...
        print(f'JobThreadLog STOPPED #{self.ident}')
        logging.info(f'JobThreadLog STOPPED #{self.ident}')