"""
Template for executables with parameters by command line.
juancarlos.miranda@uc.edu.py

Execute from terminal
$ python sequential_data1.py --parameter1 something


"""
import argparse

def usage_text():
    print('WE PUT HERE AN USAGE HELP')

def build_arg_parser():
    """
    Process parameters from command line
    :return:
    """
    parser = argparse.ArgumentParser(description='Trains the HMM-based speech recognition system')
    parser.add_argument("--parameter1", dest="var_parameter1", required=False, help="Put here help message for parameter 1")
    parser.add_argument("--parameter2", dest="var_parameter2", required=False, help="Put here help message for parameter 1")
    return parser

if __name__=='__main__':
    args = build_arg_parser().parse_args()
    input_parameter_1 = args.var_parameter1
    input_parameter_2 = args.var_parameter2

    if args.var_parameter1:
        print('args.var_parameter1-->', args.var_parameter1)
    else:
        if args.var_parameter2:
            print('args.var_parameter2-->', args.var_parameter2)
        else:
            print('WITHOUT PARAMETERS')
        pass
    pass
