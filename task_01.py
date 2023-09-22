"""
Description:
 This program calculates the factorial number from an input.
 Factorial of number

Usage:


"""


def factorial_calculation(n_to_calc):
    """
    Gets a number and returns the factorial
    1! = 1
    2! = 1*2
    3! = 1 * 2 * 3 = 6
    4! = 1*2*3*4 =24
    5! = 1*2*3*4*5 =120

    :return:
    """
    if n_to_calc < 0:
        # negative check
        n_to_calc = n_to_calc * -1

    result_factorial = 1
    count = 1

    while count <= n_to_calc:
        result_factorial = result_factorial * count
        count = count + 1

    return result_factorial


if __name__ == "__main__":
    n_input = int(input("Enter a number:"))
    result_f = factorial_calculation(n_input)  # function approach here
    print(f"Factorial = {result_f}")
    pass

