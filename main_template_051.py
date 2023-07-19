"""
Author: AUTHOR's NAME
Description:
    Here a text with an small description about the current script. It is useful for other users.
Usage:
    python main_template_01.py
"""

"""
Project: MY_PROJECT_HERE
Author: AUTHOR'S NAME HERE
Date: July 2023

Description:

Usage:
    A description of the software developed

"""


def main_function_01():
    """
    Creating a file
    Writing inside the file

    Open a file
    Reading data
    Loop reading line by line

    The Python Tutorial - 7. Input and Output - 7.2. Reading and Writing Files [https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files]

    :return:
    """
    print("I am playing with TEXT files!!!")
    file_name = "testing_writing_file.txt"
    line_to_write = "A single line to add in the file!!! \n"

    # ------------------------------
    # creating a file
    # Attention!!! 'w' for only writing (an existing file with the same name will be erased)
    # a append data to the end of the file
    with open(file_name, 'a', encoding="utf-8") as file_handler_writing:
        file_handler_writing.write(line_to_write)  # Writing inside the file
    file_handler_writing.close()
    # ------------------------------

    # ------------------------------
    # reading from file
    with open(file_name, 'r', encoding="utf-8") as file_handler_reading:
        read_data = file_handler_reading.read()  # Reading data
    file_handler_reading.close()
    # ------------------------------

    # ------------------------------
    # example to read file line by line
    # append data = 'a', only reading = 'r', only writing = 'w'
    with open(file_name, 'r+', encoding="utf-8") as file_handler_reading:
        for a_line in file_handler_reading:
            print(f"a_line={a_line}")  # Loop reading line by line
    file_handler_reading.close()
    # ------------------------------

    pass




if __name__ == "__main__":
    # single-line comment here
    print("STARTING __main__!")
    print("Now calling to the main function --> main_function_01()")
    main_function_01()
    print("After the main function --> main_function_01()")
    pass
