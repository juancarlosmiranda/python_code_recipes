"""
Author: Juan Carlos Miranda
Description:
    Script with examples using time and datetime to manage time data. Date, UTC Date, time.
    https://docs.python.org/3.8/library/datetime.html#module-datetime
    https://docs.python.org/3.8/library/time.html

    # https://stackoverflow.com/questions/17822158/how-to-get-an-utc-date-string-in-python
    # https://stackoverflow.com/questions/32402502/how-to-change-the-time-zone-in-python-logging/47104004
    # https://blog.ganssle.io/articles/2019/11/utcnow.html
    # https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc

Usage:
    python python_datetime_main.py
"""
import time
import logging
import os
from time import gmtime
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    print("Example using datetime values")

    # Measure times in seconds
    # conversion of time
    # datetimme UTC


    print("\n Examples using datetime")
    # https://docs.python.org/3.8/library/datetime.html#module-datetime
    # UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT). The acronym UTC is not a mistake but a compromise between English and French.
    # conversion from datetime to string
    datetime_now = datetime.now()
    datetime_str = datetime_now.strftime("%Y%m%d_%H%M%S_")
    time_str = datetime_now.strftime("_%H%M%S_")
    utc_time = datetime.utcnow()
    difference_utc = datetime.now() - datetime.utcnow()
    print(f"datetime_now = {datetime_now}")
    print(f"datetime_str = {datetime_str}")
    print(f"time_str = {time_str}")
    print(f"utc_time = {utc_time}")
    print(f"difference_utc = {difference_utc} hours")

    print("\n Examples using time seconds")
    # https://docs.python.org/3.8/library/time.html
    start_time = time.time()
    time.sleep(1)  # sleep one second
    end_time = time.time()
    total_time = end_time - start_time
    print(f"start_time = {start_time}")
    print(f"end_time   = {end_time}")
    print(f"total_time = {total_time}")

    print("\n Examples using nanoseconds")
    start_time = time.time_ns()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print(f"start_time = {start_time}")
    print(f"end_time   = {end_time}")
    print(f"total_time = {total_time}")

    # writing in log file
    # -----------------------------
    utc_time_now = datetime.utcnow()
    date_string = utc_time_now.strftime("%Y%m%d_%H%M%S")
    print("UTC time in str format ->", date_string)
    # -----------------------------
    print("\n Writing log file ->")
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'my_datetime_file.log')
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.DEBUG)
    logging.Formatter.converter = gmtime
    logging.debug('logging action in UTC time')
    # -----------------------------

    print("\n Calculating future dates for two days and two years ->")
    # Calculating future dates for two days and two years
    ini_time_for_now = datetime.now()
    future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
    future_date_after_2days = ini_time_for_now + timedelta(days=2)
    print('future_date_after_2yrs:', str(future_date_after_2yrs))
    print('future_date_after_2days:', str(future_date_after_2days))

# -------------------------------------
