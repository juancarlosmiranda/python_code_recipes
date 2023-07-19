"""
Author: AUTHOR's NAME
Description:
    It is a script that shows how to manage: numbers, strings, lists, dictionaries.
Usage:
    python activity_02_01.py
"""

def managing_numbers():
    print("--------------")
    print("Managing numbers")
    print("--------------")
    # For more information you can see [https://docs.python.org/3/tutorial/introduction.html#numbers]
    # From the Python console you can check the type of a variable type(a) # <class 'float'>
    a_int_01 = 1
    a_int_02 = 2
    a_float_01 = 1.0
    tax = 12.5 / 100
    price = 100.5
    calculation_01 = a_int_01 * a_float_01
    calculation_02 = price * tax
    calculation_int = int(calculation_01)

    print(f"calculation_01={calculation_01}")
    print(f"calculation_01={calculation_02}")
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
    """
    List definition.
    Access to a list element.
    Element list assignment.
    Adding elements to a list.
    Removing elements from a list.
    Sorting a list.
    Extract data from a list.

    :return:
    """

    # Lists [https://docs.python.org/3/tutorial/introduction.html#lists]
    print("--------------")
    print("Managing lists")
    print("--------------")
    a_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List definition
    print(f"a_list={a_list_of_numbers}")
    print(f"length of a_list={len(a_list_of_numbers)}")
    print(f"a_list element in position 0={a_list_of_numbers[0]}")  #  Access to a list element.
    print(f"a_list element in position 9={a_list_of_numbers[9]}")

    # assigment of a new value
    a_list_of_numbers[1] = 200
    a_list_of_letters = ['g', 'b', 'c', 'd', 'e', 'f', 'a']
    print(f"original list a_list_of_letters={a_list_of_letters}")
    a_list_of_letters[2] = 'C'  # Element list assignment.
    print(f"Changing element a_list_of_letters={a_list_of_letters}") # in order to show new assigment
    a_list_of_letters.append('h')  # Adding elements to a list.
    print(a_list_of_letters)
    last_element = a_list_of_letters.pop()  # extract the last
    print(a_list_of_letters)
    a_list_of_letters.remove('d')  # Removing elements from a list.
    print(a_list_of_letters)
    a_list_of_letters.sort()  # Sorting a list.
    print(f"sorted list a_list_of_letters={a_list_of_letters}")

    extract_values = a_list_of_letters[0: 4]  #  Extract data from a list.
    print(f"extract data from extract_values={extract_values}")

    pass

def managing_dictionaries():
    """
    Dictionary definition.
    Access to a dictionary element.
    Element dictionary assignment.
    Adding elements to a dictionary.
    Removing elements from a dictionary.
    Sorting a dictionary.

    Advanced topic to research is . 5.6. Looping Techniques

    :return:
    """
    # Dictionaries [https://docs.python.org/3/tutorial/datastructures.html#dictionaries]

    # Dictionary definition.
    a_dict = {'key_01': 100, 'key_02': 200, 'key_03': 300}
    print(f"a_dict={a_dict}")

    # Access to a dictionary element.
    value_01 = a_dict.get('key_01')
    value_02 = a_dict.get('key_02')
    print(f"value_01={value_01}")
    print(f"value_02={value_02}")

    # Element dictionary assignment.
    a_dict['key_01'] = 101
    a_dict['key_02'] = 202

    # Removing elements from a dictionary.
    a_dict.pop('key_01')
    # Sorting a dictionary.
    sorted_dict = sorted(a_dict)

    print(f"sorted_dict={sorted_dict}")
    pass

def main_function_01():
    managing_numbers()
    #managing_strings()
    #managing_lists()
    #managing_dictionaries()
    pass


if __name__ == "__main__":
    print("STARTING __main__!")
    print("Variable assigment")
    main_function_01()
    pass
