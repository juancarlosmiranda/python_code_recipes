"""
Author: AUTHOR's NAME
Description:
    This is a script with intentionally added bugs. You should fix it with the debugging tool.
Usage:
    python activity_02_03.py
"""

def fixme_numbers():
    print("--------------")
       print("Managing numbers")
    print("--------------")
       # For more information you can see [https://docs.python.org/3/tutorial/introduction.html#numbers]
    # From the Python console you can check the type of a variable type(a) # <class 'float'>
    a_int_01 = 1
    a_int_02 = 2
  a_float_01 = 1.0
    tax = 0
    price = 100.5
    calculation_01 = a_int_01 * a_float_01
     calculation_02 = price / tax
    calculation_int = int(calculation_01)

    print(f"calculation_01={calculation_01}")
    print(f"calculation_01={calculation_02}")
    print(f"calculation_int={calculation_int}")


def main_fixme_01():
    fixme_numbers()
    pass


if __name__ == "__main__":
    print("FIX ME __main__!")
    main_fixme_01()
    pass
