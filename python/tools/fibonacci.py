#
# Vincent Charming (c) 2025
#
"""
Task: Print out the first 20 numbers in the fibonacci series.
"""

__author__ = "vcharming"

import argparse
import logging
import sys

# Initialize logger config
logger = logging.getLogger(__name__)
LOG_FORMAT = "[%(filename)s:%(lineno)s - %(levelname)-5s ] %(message)s"
logging.basicConfig(format=LOG_FORMAT)
logger.setLevel(logging.DEBUG)


def get_fibonacci(n: int, reverse_sequence: bool = False) -> list:
    """
    Returns the fibonacci sequence to n places
    :param n: A positive integer for the number of places of the fibonacci sequence
    :param reverse_sequence: Flag to reverse the fibonacci sequence
    :return: A list of the fibonacci sequence
    """
    # Data Validation
    error_message = "Parameter must be a positive integer."
    if not isinstance(n, int):
        raise TypeError(error_message)
    if n <= 0:
        raise ValueError(error_message)

    current_num_behind_2, current_num_behind_1, current_num  = 0, 1, 1
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(current_num)
        current_num = current_num_behind_2 + current_num_behind_1
        current_num_behind_2 = current_num_behind_1
        current_num_behind_1 = current_num
    if reverse_sequence:
        logger.info("Reversing the fibonacci sequence.")
        fibonacci_sequence.reverse()    # O(n)
    return fibonacci_sequence


def init_parser():
    """
    Initialize an argument parser for command line options

    :return An instance of argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(description="Print the fibonacci series to the nth place")

    parser.add_argument(
        "num_of_places",
        help="The number of places to print out the fibonacci sequence.")

    parser.add_argument(
        "--reverse-sequence",
        action="store_true",
        help="Reverses the output of the fibonacci sequence.")

    return parser


def main(args):
    """
    Print the fibonacci series to the nth place
    :param args: The parsed command line arguments
    """

    logger.info(f"Getting the fibonacci sequence to {args.num_of_places} places.")
    fibonacci_sequence = get_fibonacci(int(args.num_of_places), args.reverse_sequence) # O(n)
    for fibonacci_num in fibonacci_sequence:
        logger.info(fibonacci_num)

    sys.exit()


if __name__ == "__main__":
    p = init_parser()
    sys.exit(main(p.parse_args()))
