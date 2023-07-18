"""
Author: AUTHOR's NAME
Description:
    Here a script to show different type of data used in Python
Usage:
    python main_template_01.py
"""

def managing_numbers():
    print("--------------")
    print("Managing numbers")
    print("--------------")
    # for more information you can see [https://docs.python.org/3/tutorial/introduction.html#numbers]
    # From the Python console you can check the type of a variable type(a) # <class 'float'>
    a_int_01 = 1
    a_int_02 = 2
    a_float_01 = 1.0
    tax = 12.5 / 100
    price = 100.5
    calculation_01 = price * tax
    calculation_int = int(calculation_01)

    print(f"calculation_01={calculation_01}")
    print(f"calculation_int={calculation_int}")


def managing_strings():
    print("--------------")
    print("--------------")
    print("Managing strings")
    print("--------------")
    # Managing string variables
    # Check [https://docs.python.org/3/tutorial/introduction.html#strings]
    string_01 = 'my string with single quotes'
    string_02 = "my string with double quotes"

    print(f"string_01={string_01}")
    print(f"string_02={string_02}")

    # example of a string with multiple lines
    print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)

    print("Access to elements inside a variable string:")
    print(f"String value = {string_01}")
    print(f"String length = {len(string_01)}")
    print(f"String value in position 3 = {string_01[3]}")
    # assigment of a new value
    #string_02[0] = 'M'  # strings are inmutable ERROR
    string_03 = 'M' + string_02[1:]  # assigment suggested by official site

    # printing new value
    print(string_01)
    print(string_03)

    # printing parts of a string value
    print(string_01[3:])
    print(string_01[:8])
    print(string_01[3:5])

def managing_lists():
    # Lists [https://docs.python.org/3/tutorial/introduction.html#lists]
    print("--------------")
    print("Managing lists")
    print("--------------")
    a_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"a_list={a_list_of_numbers}")
    print(f"length a_list={len(a_list_of_numbers)}")
    print(f"a_list in position 0={a_list_of_numbers[0]}")
    print(f"a_list in position 9={a_list_of_numbers[9]}")

    # assigment of a new value
    a_list_of_numbers[1] = 200
    a_list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(a_list_of_letters)
    a_list_of_letters[2] = 'C'
    print(a_list_of_letters) # in order to show new assigment
    # tricks to manage lists
    # a_list_of_letters[start_position: end_position]
    # todo_ add a list of words

    pass

def managing_dictionaries():
    raise to implement
    pass

def main_function_01():
    managing_numbers()
    managing_strings()
    managing_lists()
    managing_dictionaries()
    pass


if __name__ == "__main__":
    print("STARTING __main__!")
    print("Variable assigment")
    main_function_01()
    pass
