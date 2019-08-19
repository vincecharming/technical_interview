#
# Vincent Charming (c) 2019
#
"""
Question for SWE I Interview
Task: Print out the first 20 numbers in the fibonacci series.
"""

__author__ = 'vcharming'

import argparse
import logging
import sys

# Initialize logger config
logger = logging.getLogger(__name__)
LOG_FORMAT = '[%(filename)s:%(lineno)s - %(levelname)-5s ] %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger.setLevel(logging.DEBUG)


def print_fibonacci(n):
    '''
    Prints the fibonacci sequence to n places
    :param n: positive integer
    :return:
    '''
    # Data Validation
    error_message = 'Parameter must be a positive integer.'
    if not isinstance(n, int):
        raise TypeError(error_message)
    if n <= 0:
        raise ValueError(error_message)
    
    current_num_behind_2, current_num_behind_1, current_num  = 0, 1, 1
    for i in range(n):
        logger.info(current_num)
        current_num = current_num_behind_2 + current_num_behind_1
        current_num_behind_2 = current_num_behind_1
        current_num_behind_1 = current_num
    return


def init_parser():
    '''
    Initialize an argument parser for command line options

    :return An instance of argparse.ArgumentParser
    '''

    parser = argparse.ArgumentParser(description="Print the fibonacci series to the nth place")

    parser.add_argument(
        "num_of_places",
        help="The number of places to print out the fibonacci sequence.")

    return parser


def main(args):
    '''
    Print the fibonacci series to the nth place
    :param args: The parsed command line arguments
    '''

    print_fibonacci(int(args.num_of_places))

    sys.exit()


if __name__ == '__main__':
    p = init_parser()
    sys.exit(main(p.parse_args()))