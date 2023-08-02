"""
Run a UI with options for launch threads
python ui_main_thread_01.py
"""

import logging
import time
from job_thread_log import JobThreadLog


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Service Exit --> \r')
    pass

def service_shutdown(signum, frame):
    print('Service shut down --> Caught signal %d' % signum)
    raise ServiceExit

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', filename='threadlogger.log', level=logging.DEBUG)
    try:
        j1 = JobThreadLog()
        j1.start()
        time.sleep(5)
        j1.shutdown_flag.set()
        j1.join()

    except ServiceExit:
        print('ServiceExit Exception --> ')
        print('CATCHING any Exception HERE!-->')
        j1.shutdown_flag.set()
        j1.join()
