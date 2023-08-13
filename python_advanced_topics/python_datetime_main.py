"""
Author: Juan Carlos Miranda
Description:
    Script with examples using time and datetime in order to manage that type of data
    https://docs.python.org/3.8/library/datetime.html#module-datetime
    https://docs.python.org/3.8/library/time.html

Usage:
    python python_datetime_main.py
"""
import time
from datetime import datetime

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

# -------------------------------------
