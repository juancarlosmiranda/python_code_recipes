"""
Author: AUTHOR's NAME
Description:
    Here a script to show different control flow sentences
    The Python Tutorial - More Control Flow Tools - 4.6. match Statements. [https://docs.python.org/3/tutorial/controlflow.html#match-statements]

Usage:
    python activity_01_01.py
"""

# requirement Python > 3.10
def main_control_flow_sentences():
    # simple user input here
    print("Show control flow sentences!")
    user_input = int(input("Enter a number here >>"))
    print(f"The user entered = {user_input}")
    # this code works on python >= 3.10
    match user_input:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")
    pass


if __name__ == "__main__":
    print("Starting __main__!")
    main_control_flow_sentences()
    pass
