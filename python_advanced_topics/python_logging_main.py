"""
Author: Juan Carlos Miranda
Description:
    Script to show logging in files, using info, warning aand debug message

Usage:
    python python_logging_main.py
"""
import logging

if __name__ == '__main__':
    print("Example using logging messages")
    message_text = "PRINTING MESSAGE ->"
    # -------------------------------------
    # evel=logging.DEBUG, evel=logging.INFO, evel=logging.WARNING
    logging.basicConfig(format='%(asctime)s %(message)s', filename='python_logging_main.log', level=logging.DEBUG)
    logging.info('STARTED #%s' % message_text)
    logging.warning(f'WORKING #{message_text}')
    logging.debug(f'STOPPED #{message_text}')
