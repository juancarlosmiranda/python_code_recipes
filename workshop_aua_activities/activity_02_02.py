"""
Author: AUTHOR's NAME
Description:
    It is a script that shows the scope of the variables inside a program.
Usage:
    python activity_02_02.py
"""



def other_stuff():
    """
    :return:
    """
    print("other_stuff()->")
    pass

def main_function_01():
    variable_inside_function = 1
    print(f"variable_inside_function={variable_inside_function}")
    other_stuff()
    variable_inside_function = 2
    print(f"variable_inside_function={variable_inside_function}")
    global_variable = "The same name inside function"
    print(f"global_variable={global_variable}")
    pass

global_variable = "I am a global variable"

if __name__ == "__main__":
    print("Variable scope -->")
    print(f"Before main_function_01() -> global_variable={global_variable}")
    main_function_01()
    print(f"After main_function_01() -> global_variable={global_variable}")
    global_variable = "Changed"
    print(f"Changing main_function_01() -> global_variable={global_variable}")
    pass
