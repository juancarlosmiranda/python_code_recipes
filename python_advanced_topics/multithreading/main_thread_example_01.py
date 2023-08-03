"""
Author: Juan Carlos Miranda
Description:
    Threading implementing as class with logging instructions

Usage:
    python main_thread_example_01.py

"""
import time
import threading
import signal


class ThreadTask(threading.Thread):
    """
    Class representing a task that inherits methods for threading
    """
    def __init__(self):
        threading.Thread.__init__(self)
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
        # ... Other thread setup code here ...
        print("Initializing data here -->")

    def run(self):
        print("Thread #%s started" % self.ident)

        # meanwhile is running
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            print("--> Thread #%s running" % self.ident)
            time.sleep(0.5)

        # ... Clean shutdown code here ...
        print("Thread #%s stopped" % self.ident)


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print("Service Exit -->")
    pass


def service_shutdown(signum, frame):
    print("Service shut down --> Caught signal %d" % signum)
    raise ServiceExit



def main():
    # Register the signal handlers
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
    print("Starting main program \n")

    # Start the job threads
    try:
        j1 = ThreadTask()  # creating the first task
        j2 = ThreadTask()  # creating the second task
        j1.start()  # starting the first task
        j2.start()  # starting the second task

        # Keep the main thread running, otherwise signals are ignored.

        while True:
            print("Entering in infinite loop -> \n")
            time.sleep(0.5)

    except ServiceExit:
        # Terminate the running threads.
        # Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
        print("ServiceExit Exception -->")
        j1.shutdown_flag.set()
        j2.shutdown_flag.set()
        # Wait for the threads to close...
        j1.join()
        j2.join()

    print('Exiting main program')


if __name__ == '__main__':
    print("Hello threads example!!! \n")
    main()
