"""
Author: Juan Carlos Miranda
Description:
    Load settings from a file and save it in files
    configparser — Configuration file parser
    https://docs.python.org/3/library/configparser.html


Usage:
    python python_load_config_from_files.py
"""

import os
import configparser

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_config_file_r = os.path.join(BASE_DIR, 'client_settings_r.conf')
    path_config_file_w = os.path.join(BASE_DIR, 'client_settings_w.conf')

    # ----------------------------------------------------
    # Read data fro file
    f_config_r = configparser.ConfigParser()
    # by default from client_settings_r.conf
    f_config_r.read(path_config_file_r)
    protocol = f_config_r['DEFAULT']['protocol']
    host = f_config_r['DEFAULT']['host']
    port = f_config_r['DEFAULT']['port']
    user = f_config_r['DEFAULT']['user']
    password = f_config_r['DEFAULT']['password']
    sleep_time = int(f_config_r['DEFAULT']['sleep_time'])
    path_video_output = f_config_r['DEFAULT']['path_video_output']

    # ----------------------------------------------------
    # Showig data read
    print("Settings read from file")
    print("protocol          ->", protocol)
    print("host              ->", host)
    print("port              ->", port)
    print("user              ->", user)
    print("password          ->", password)
    print("sleep_time        ->", sleep_time)
    print("path_video_output ->", path_video_output)

    # ----------------------------------------------------
    # Saving data
    print("Saving settings in file")
    f_config_w = configparser.ConfigParser()
    f_config_w['DEFAULT']['protocol'] = protocol
    f_config_w['DEFAULT']['host'] = host
    f_config_w['DEFAULT']['port'] = port
    f_config_w['DEFAULT']['user'] = user
    f_config_w['DEFAULT']['password'] = password
    f_config_w['DEFAULT']['sleep_time'] = str(sleep_time)
    f_config_w['DEFAULT']['path_video_output'] = path_video_output

    # Writing our configuration file to 'example.conf'
    with open(path_config_file_w, 'w') as configfile:
        f_config_w.write(configfile)
    print(f"Check settings saved in {path_config_file_w }")