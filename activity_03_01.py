"""
Author: AUTHOR's NAME
Description:
    Here a script to show different control flow sentences
    The Python Tutorial - More Control Flow Tools - 4.1. if Statements. [https://docs.python.org/3/tutorial/controlflow.html#if-statements]

Usage:
    python activity_03_01.py
"""


def main_control_flow_sentences():
    # simple user input here
    print("Show control flow sentences!")
    user_input = int(input("Enter a number here >>"))
    print(f"The user entered = {user_input}")

    # user input to be processed with control flows
    a_number = int(input("a_number="))

    # relational operators
    #  > (greather than), < (less than), == (equal to), >= (greather than or equal), <= (less than or equal), != (distintc)
    if a_number < 0:
        print(f"a_number less than 0 {a_number} NEGATIVE NUMBER!")
    else:
        print(f"possible a_number is equal to 0 or is greater than 0 {a_number}")
        if a_number == 0:
            print(f"a_number equal to cero {a_number}")
        else:
            print(f"a_number greater than cero {a_number} POSITIVE NUMBER!")
        pass  # I put this to organise the code, this sentence is not necessary
    pass

    # logic operators
    # and, or, not. See true table
    if (user_input == 0) and (a_number > 0):
        print("user_input == 0 and a_number is a POSITIVE NUMBER")
    else:
        print("something is not fullfiling the condition!")

    pass


if __name__ == "__main__":
    print("Starting __main__!")
    main_control_flow_sentences()
    pass
