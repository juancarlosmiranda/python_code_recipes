"""
Author: Juan Carlos Miranda
Description:
    Script to run a shell command detecting Windows or Linux operating systems.
    Based on https://janakiev.com/blog/python-shell-commands/

Usage:
    python python_execute_shell_cmd.py
"""
import os
import sys
import subprocess


if __name__ == '__main__':

    win_cmd_to_execute = 'DIR /D'
    linux_cmd_to_execute = 'ls -l'

    # checking the platform using sys
    if sys.platform == "win32":
        print("Detected Windows family")
        print(f"Shell command execution in {sys.platform}")
        win_cmd_to_execute = 'DIR /D'
        os.system(win_cmd_to_execute)  # call to shell command
        stream = os.popen('echo Returned output')
        output = stream.readlines()
        print("-->", output)

    elif sys.platform == "linux":
        print(f"Shell command execution in {sys.platform}")
        process = subprocess.Popen(linux_cmd_to_execute.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)

        # second option using os.system call
        print("command execution 2)")
        os.system(linux_cmd_to_execute)  # call to shell command
        stream = os.popen('echo Returned output')
        output = stream.readlines()
        print("-->", output)
