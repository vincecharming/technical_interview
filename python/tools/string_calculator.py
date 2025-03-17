#
# Vincent Charming (c) 2025
#
'''
Task: Design a calculator to compute an arithmetic string, i.e. '1 + 1' => 2
1. What are the primary components that a system like this needs in order
   to function correctly?  Think about this in terms of simple classes or
   functions that can break up the problem space into tractable components.
2. What's a really easy "MVP" you think you can write in the span of ~35
   minutes?
3. Take a shot at implementing your MVP in your language of choice.

Example input:output in order of difficulty:
'1 * 1'              : 1
'1 + -1'             : 0
'1 + 4 - 2'          : 3
'1 * 10 - 7 / 4'     : 8.25
'(1 * 10) - (7 / 4)' : 8.25
'10 - 1.75'          : 8.25

MVP does not address exponents or mulitplication without the symbol
'''

import logging
import unittest

# Initialize logger config
logger = logging.getLogger(__name__)
LOG_FORMAT = '[%(filename)s:%(lineno)s - %(levelname)-5s ] %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger.setLevel(logging.INFO)

def contains_mul_div_operands(s):
    if (s.find('*') + s.find('/')) == -2:
        return False
    else:
        return True

def contains_add_sub_operands(s):
    if (s.find('+') + s.find('-')) == -2:
        return False
    else:
        return True

def str_calc_simple(str_1: str, str_2: str, operand: str):
    '''
    Performs a calculation and returns the result.
    :param str_1: A number as a string
    :param str_2: A number as a string
    :param operand: An operand as a string
    :return: The calculated result
    '''
    # TODO Data Validation
    if '.' in str_1 or '.' in str_2:
        num_1, num_2 = float(str_1), float(str_2)
    else:
        num_1, num_2 = int(str_1), int(str_2)
    
    if operand == '+':
        return num_1 + num_2
    elif operand == '-':
        return num_1 - num_2
    elif operand == '*':
        return num_1 * num_2
    elif operand == '/':
        if num_2 == 0:
            raise ValueError('Cannot divide by 0.')
        return num_1 / num_2
    else:
        raise ValueError('Operand must be \'+\', \'-\', \'*\', or \'/\'')


def find_bounds(s, mid_index):
    left_index, right_index = 0, len(s) - 1
    # This flag is used to avoid spaces around the middle index (i.e. operand)
    inside_number = False
    for i in range(mid_index - 1, -1, -1):
        try:
            int(s[i])
            inside_number = True
        except ValueError:
            if (s[i] == ' ' and not inside_number) or s[i] == '.' or s[i] == '-':
                continue
            left_index = i
            break
    
    inside_number = False
    for i in range(mid_index + 1, len(s)):
        try:
            int(s[i])
            inside_number = True
        except ValueError:
            if (s[i] == ' ' and not inside_number) or s[i] == '.' or s[i] == '-':
                continue
            right_index = i - 1
            break

    return left_index, right_index


def str_calculator(s, op_1='*', op_2='/'):
    '''
    Finds the answer to a mathematics problem from a string.
    :param s: An equation as a string
    :return: The answer to the problem
    '''
    # Data Validation
    if not isinstance(s, str):
        raise TypeError('Parameter must be the equation as a string.')
    if not s:
        raise ValueError('Parameter must be a populated string.')

    result = 0

    mid_index_mult = s.find(op_1)
    mid_index_div = s.find(op_2)
    # If both are present, then we must traverse left to right
    if not mid_index_mult == -1 and not mid_index_div == -1:
        if mid_index_mult < mid_index_div:
            mid_index = mid_index_mult
        else:
            mid_index = mid_index_div
    elif not mid_index_mult == -1:
        mid_index = mid_index_mult
    elif not mid_index_div == -1:
        mid_index = mid_index_div
    else:
        return result

    left, right = find_bounds(s, mid_index)
    logger.debug(s[left:mid_index_mult])
    logger.debug(s[mid_index_mult+1:right+1])
    result = str_calc_simple(s[left:mid_index], s[mid_index+1:right+1], s[mid_index])
    logger.debug(result)
    new_s = s[0:left] + str(result) + s[right+1:len(s)]
    if contains_mul_div_operands(new_s):
        result = str_calculator(new_s, '*', '/')
    elif contains_add_sub_operands(new_s):
        result = str_calculator(new_s, '+', '-')
    else:
        return result

    return result

'''
TODO: @vcharming The unit test below should be in a separate file run set to run at a specific cadence and or
as a blocker to any related diffs to this util
'''
class TestCalculator(unittest.TestCase):
    def test_contains_mul_div_operands(self):
        test_strs_and_results = [
            ('1 * 1', True),
            ('1 * 1', True),
            ('4/9', True),
            ('1  1', False),
            ('1 + 1', False)]
        for test_str, result in test_strs_and_results:
            if result:
                self.assertTrue(contains_mul_div_operands(test_str))
            else:
                self.assertFalse(contains_mul_div_operands(test_str))

    def test_contains_add_sub_operands(self):
        test_strs_and_results = [
            ('1 + 1', True),
            ('1 - 1', True),
            ('4+9', True),
            ('1  1', False),
            ('1 * 1', False)]
        for test_str, result in test_strs_and_results:
            if result:
                self.assertTrue(contains_add_sub_operands(test_str))
            else:
                self.assertFalse(contains_add_sub_operands(test_str))

    def test_str_calc_simple(self):
        test_arrays_and_results = [
            (['10', '/', '2'], 5),
            (['10', '/', '2'], 5),
            (['10', '*', '2.5'], 25),
            (['12', '+', '4'], 16),
            (['12', '-', '4'], 8)]
        for test_arr, result in test_arrays_and_results:
            self.assertEqual(str_calc_simple(test_arr[0], test_arr[2], test_arr[1]), result)
        self.assertRaises(ValueError, lambda: str_calc_simple('1', '0', '/'))
        self.assertRaises(ValueError, lambda: str_calc_simple('4', '2', '^'))

    def test_str_calculator(self):
        test_strs_and_results = {
            '10 / 2 * 4': 20,
            '10 * 2 / 4': 5,
            '10 * 2 * 4': 80,
            '10 * 2 + 4': 24,
            '10 + 2 * 4': 18}
            #'1 * 1': 1
            #'40 - 2 * 10 + 5': 25
            #'1 + -1': 0,
            #'1 + 4 - 2': 3,
            #'1 * 10 - 7 / 4': 8.25,
            #'(1 * 10) - (7 / 4)': 8.25,
            #'10 - 1.75': 8.25}
        for test_str, result in test_strs_and_results.items():
            self.assertEqual(str_calculator(test_str), result)
        self.assertRaises(TypeError, lambda: str_calculator(10+1))
        self.assertRaises(ValueError, lambda: str_calculator(''))

def suite():
    functions_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    return unittest.TestSuite([functions_suite])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run(suite())
