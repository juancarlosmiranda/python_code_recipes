"""
Author: AUTHOR's NAME
Description:
    Here a script to show different control flow sentences
    Python 4. More Control Flow Tools - 8.3. The for statement [https://docs.python.org/3/reference/compound_stmts.html#the-for-statement]

Usage:
    python main_template_01.py
"""


def main_control_flow_sentences():
    # simple user input here
    print("Show control flow sentences!")
    print("while and for")

    # ---------------------
    # simple example for
    for i in range(10):
        print(f"i={i}")
    # ---------------------

    # ---------------------
    an_animals_list = ['cat', 'dog', 'elephant', 'seal', 'monkey']
    for an_animal in an_animals_list:
        print(f"an_animal={an_animal}")
    # ---------------------

    # ---------------------
    an_animals_list = ['cat', 'dog', 'elephant', 'seal', 'monkey']
    for an_animal in an_animals_list:
        print(f"an_animal={an_animal}")
        if an_animal == 'dog':
            # you can add the function that you want here
            print("Ohhh it is a DOG!")
    # ---------------------

    pass


if __name__ == "__main__":
    print("Starting __main__!")
    main_control_flow_sentences()
    pass
