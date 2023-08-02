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
# \n
    def run(self):
        print('\n Job --> Thread #%s started \r' % self.ident)

        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            print(f'Job -->#{self.ident} \r')
            time.sleep(0.5)

        # ... Clean shutdown code here ...
        print('Job --> Thread #%s stopped \r' % self.ident)