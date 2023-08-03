"""
Author: Juan Carlos Miranda
Description:
    Implementation of threads as a class with register statements.
    This script shows the sequence of how to start a process and how to stop it.

Usage:
    python main_thread_example_01.py

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
        j1.start()  # start running
        time.sleep(5)  # sleep for 5 seconds
        j1.shutdown_flag.set()  # shutdown the process
        j1.join()  # stopping

    except ServiceExit:
        print('ServiceExit Exception --> ')
        print('CATCHING any Exception HERE!-->')
        j1.shutdown_flag.set()
        j1.join()
