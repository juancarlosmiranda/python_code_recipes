"""
Author: AUTHOR's NAME HERE
Description:
    Here a text with an small description about the current script. It is useful for other users.
    This scripts shows different types fo functions, with parameters inputs and outputs.
Usage:
    python main_template_022.py
"""


def my_function_stuff_01():
    print("This function do a lot of amazing calculations!!!")
    print("Doesn't return any result!!!")
    pass


def my_function_stuff_02(input_par_01, input_par_02):
    print("This function do a lot of amazing calculations!!!")
    print("Doesn't return any result!!!")
    print(f"input_par_01={input_par_01}")
    print(f"input_par_02={input_par_02}")
    pass  # null instruction do nothing


def my_function_stuff_03(input_par_01, input_par_02):
    """
    This function do something ....
    input_par_01: useful for bla bla
    input_par_02: useful for bla bla

    :returns: factor_01, factor_02
    """
    inside_01 = 1
    inside_02 = 1
    factor_01 = 0
    factor_02 = 0
    print("This function do a lot of amazing calculations!!!")
    print("Receives parameters and return any result!!!")
    factor_01 = inside_01 * input_par_01
    factor_02 = inside_02 * input_par_02
    return factor_01, factor_02


def main_function_01():
    print("I AM INSIDE THE MAIN FUNCTION")
    pass
    pass  # null instruction do nothing


#  starting point
if __name__ == "__main__":
    """
    A multi-line comment 
    """
    # example of a single-line comment
    print("STARTING __main__!")
    print("Now calling to the main function --> main_function_01()")
    main_function_01()  # without parameters
    print("After the main function --> main_function_01()")
    input_p_01 = 1  # definition of variables
    input_p_02 = 2
    print("Now calling to the main function --> main_function_02()")
    my_function_stuff_02(input_p_01, input_p_02)
    print("After the main function --> main_function_02()")
    print("Now calling to the main function --> main_function_03()")
    res_01, res_02 = my_function_stuff_03(input_p_01, input_p_02)
    print("After the main function --> main_function_03()")
    pass
