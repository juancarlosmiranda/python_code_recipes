"""
Author: Juan Carlos Miranda
Description:
    Script to show logging in files, using info, warning and debug messages.

Usage:
    python python_logging_main.py
"""
import logging
import os
from time import gmtime

if __name__ == '__main__':
    print("Example using logging messages")
    message_text = "PRINTING MESSAGE ->"
    # -------------------------------------
    # evel=logging.DEBUG, evel=logging.INFO, evel=logging.WARNING
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'python_logging_main.log')
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.DEBUG)
    logging.Formatter.converter = gmtime
    logging.info('STARTED #%s' % message_text)
    logging.warning(f'WORKING #{message_text}')
    logging.debug(f'STOPPED #{message_text}')
    # ---- PRINT ONLY DEBUG INFO ----
    logging.debug('1) first log')
    logging.debug('2) second log')
    logging.debug('3) third log')