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
    # simple example while
    i = 0
    END_I = 10
    while i < END_I:
        print(f"i={i}")
        i = i + 1
    # ---------------------

    # ---------------------
    # simple example while
    i = 0
    j = 0
    END_I = 4
    END_J = 4
    while i < END_I:
        # ------------
        j = 0  # what happen if I comment this line?
        while j < END_J:
            print(f"i={i}, j={j}")
            # -------------------------
            # DO something HERE!
            # -------------------------
            j = j + 1  # don't forget the counter!!
        # ------------
        i = i + 1
    # ---------------------
    pass


if __name__ == "__main__":
    print("Starting __main__!")
    main_control_flow_sentences()
    pass
