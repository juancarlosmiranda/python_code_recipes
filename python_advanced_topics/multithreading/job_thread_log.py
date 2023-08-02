import time
import threading
import logging

class JobThreadLog(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        # \n

    def run(self):
        print('STARTED #%s' % self.ident)
        logging.info('STARTED #%s' % self.ident)
        while not self.shutdown_flag.is_set():
            print(f'WORKING #{self.ident}')
            logging.info(f'WORKING #{self.ident}')
            time.sleep(1)

        # ... Clean shutdown code here ...
        print(f'STOPPED #{self.ident}')
        logging.info(f'STOPPED #{self.ident}')