def main_function_01():
    print("I am the main function Hi!!!")
    a_var_int = int(input("A_VAR_INT input a number:"))
    b_var_int = int(input("B_VAR_INT input a number:"))

    print(f"a_var_int={a_var_int}")
    print(f"b_var_int={b_var_int}")

    if a_var_int < b_var_int:
        print(f"The gratest is {b_var_int}")
        print("The gratest is", b_var_int)
    else:
        print(f"The gratest is {a_var_int}")
        print("The gratest is", a_var_int)


pass

if __name__ == "__main__":
    # single-line comment here
    print("STARTING __main__!")
    print("Now calling to the main function --> main_function_01()")
    main_function_01()
    print("After the main function --> main_function_01()")

    pass
