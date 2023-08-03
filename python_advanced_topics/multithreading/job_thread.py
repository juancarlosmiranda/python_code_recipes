"""
Author: Juan Carlos Miranda
Description:
    Threading implementing as class

Usage:
    j1 = JobThreadLog()
    j1.start()

"""
import time
import threading
import signal

class JobThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
        # ... Other thread setup code here ...

    def run(self):
        print('\n JobThread --> Thread #%s started \r' % self.ident)
        # meanwhile the flag is set
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            print(f'JobThread -->#{self.ident} self.shutdown_flag.is_set()={self.shutdown_flag.is_set()}\r')
            time.sleep(0.5)

        # ... Clean shutdown code here ...
        print('JobThread --> Thread #%s stopped \r' % self.ident)
