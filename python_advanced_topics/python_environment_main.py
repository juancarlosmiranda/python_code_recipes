"""
Author: Juan Carlos Miranda
Description:
    Script with examples system variables.
    This checks if the script is running under Windows and show variables
    https://www.geeksforgeeks.org/python-os-environ-object/

Usage:
    python python_environment_main.py
"""
import os
import sys

if __name__ == '__main__':
    print("Examples getting data from Operating Systems")
    environment_info = None

    # checking the platform using sys
    if sys.platform == "win32":
        print("Detected Windows family")
        # here access to operating system environment
        # the environment variables changes between operating systems
        # description for Windows variables can be found here
        # Environment variables for Windows 10
        # https://learn.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables
        environment_info = os.environ

        print(f"platform = {sys.platform}")
        print(f"OS = {environment_info['OS']}")
        print(f"COMPUTERNAME    = {environment_info['COMPUTERNAME']}")
        print(f"USERNAME        = {environment_info['USERNAME']}")
        print(f"USERPROFILE     = {environment_info['USERPROFILE']}")
        print(f"USERDOMAIN      = {environment_info['USERDOMAIN']}")
        print(f"ALLUSERSPROFILE = {environment_info['ALLUSERSPROFILE']}")
        print(f"APPDATA         = {environment_info['APPDATA']}")
        print(f"LOCALAPPDATA    = {environment_info['LOCALAPPDATA']}")
        print(f"HOMEDRIVE       = {environment_info['HOMEDRIVE']}")
        print(f"HOMEPATH        = {environment_info['HOMEPATH']}")
        print(f"LOGONSERVER     = {environment_info['LOGONSERVER']}")
        print(f"COMSPEC         = {environment_info['COMSPEC']}")

    # checking the platform using sys
    if sys.platform == "linux":
        print("Detected Linux family")
        print("DOING SOMETHING")
        print(f"USERNAME        = {environment_info['USERNAME']}")
        print(f"HOSTNAME        = {environment_info['HOSTNAME']}")
        print(f"HOME            = {environment_info['HOME']}")
        print(f"SHELL           = {environment_info['SHELL']}")
    # --------





    # --------------------------------

    # -----------------------------------------
