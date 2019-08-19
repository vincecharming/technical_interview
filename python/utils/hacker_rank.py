#
# Vincent Charming (c) 2019
#
"""
HackerRank Sample Problems
"""

import bisect
import unittest

from collections import Counter, defaultdict

__author__ = 'vcharming'

'''
Given 2 arrays (sorted & distinct) find the number of elements in common.
'''
def get_num_common_in_array(arr_1, arr_2):
    '''
    Returns the number of common elemnts found in 2 distinct sorted arrays
    The arrays are assumed to be sorted (i.e. not validated)
    :param arr_1: A sorted array
    :param arr_2: A sorted array distinct from the first array
    :return: Number of common elements
    '''
    # Data Validation on params
    error_message = 'Parameters must be populated distinct sorted arrays'
    if not (isinstance(arr_1, list) and isinstance(arr_2, list)):
        raise TypeError(error_message)
    if (not arr_1) or (not arr_2):
        raise ValueError(error_message)

    num_common_elements = 0
    arr_2_last_index = 0
    for i, arr_1_element in enumerate(arr_1):
        # Skips duplicate values within the first array
        if (not i == 0) and (arr_1_element == arr_1[i - 1]):
            continue
        '''
        # This method is not as optimal but will work
        if arr_1_element in arr_2:
            num_common_elements += 1
        '''
        # Because the arrays are sorted, we are able to walk through the second array in parallel -> O(n)
        for j, arr_2_element in enumerate(arr_2[arr_2_last_index:]):
            # Skips the remainder of the array that will surely not match the value in question
            if arr_1_element < arr_2_element:
                break
            else:
                if arr_1_element == arr_2_element:
                    num_common_elements += 1
                # Updates the last index for the start of the next interation of the second array
                arr_2_last_index = j + 1

    return num_common_elements


'''
Given a number as an array, with each digit as an element, add 1. Assume the number given is positve.
Ex. 284 + 1 = 285 > [2, 8, 4] would return [2, 8, 5]
Ex. 9 + 1 = 10 > [9] would return [1, 0]
'''
def add_one_to_array_num(num_arr):
    '''
    Adds 1 to a number given as an array
    :param num_arr: A number as an array, where each value is a positive 0-9 integer
    :return: The number plus 1 as an array
    '''
    # Data Validation on param
    error_message = 'The input must be a number as an array. Example: 412 would be [4, 1, 2].'
    if not isinstance(num_arr, list):
        raise TypeError(error_message)
    if not num_arr:
        raise ValueError(error_message)

    # Iterating reversed through the indices allows us to start at the one's place and work up
    for j in reversed(range(len(num_arr))):
        # Accounts for carrying the 1 to the next place over
        if (num_arr[j] + 1) == 10:
            num_arr[j] = 0
            # Accounts for having to carry the one all the way to start of the array
            if j == 0:
                num_arr.insert(j, 1)
        else:
            num_arr[j] += 1
            break

    return num_arr


'''
Find the largest sum of an hourglass pattern as defined below
a b c
  d
e f g
Ex. Function returns 7 for the matrix below
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
'''
def hourglass_sum(arr):
    '''
    Returns the largest sum of an hourglass shape as defined below
    :param arr: A 2D array that is at least 3x3
    :return: The largest sum of an hourglass shape within the matrix
    '''
    # Enforces a 3x3 or larger matrix
    if len(arr) < 3 or len(arr[0]) < 3:
        raise ValueError('Func hourglass_sum() requires a 3x3 matrix')

    for j in range(len(arr) - 2):
        for i in range(len(arr[0]) - 2):
            temp_sum = arr[j][i] + arr[j][i + 1] + arr[j][i + 2] + \
                arr[j + 1][i + 1] + \
                arr[j + 2][i] + arr[j + 2][i + 1] + arr[j + 2][i + 2]
            # On the first pass, the result gets set to the value of the hourglass as a baseline
            if j == 0:
                result = temp_sum
            elif temp_sum > result:
                result = temp_sum
    return result


'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream.
On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.
Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny
choose two distinct flavors such that they spend their entire pool of money during each visit.
Return ID numbers for the two types of ice cream that Sunny and Johnny purchase. Return the smaller ID first and
the larger ID second.
Ex. n = 5, cost = [1, 4, 5, 3, 2], money = 4 would return (1, 4) because at the costs at those indexes are (1, 3),
which add up to 4
Ex. n = 4, cost = [2, 2, 4, 3], money = 4 would return (1, 2) because 2 + 2 = 4
'''
def what_flavors(cost, money):
    '''
    Return an ordered pair of indexes (starting at 1) that correspond with the spending the entire money amount
    :param cost: An unsorted array of prices
    :param money: The total amount of money that must be spent
    :return: An ordered pair of indexes from the cost array (starting at 1)
    '''
    remainder_arr = {}
    index_1 = 0
    index_2 = 0
    for i, price in enumerate(cost):
        if price > money:
            continue
        remainder = money - price
        try:
            index_1 = remainder_arr[price]
            # Puts the smaller index first
            if (i + 1) < index_1:
                index_2 = index_1
                index_1 = i + 1
            else:
                index_2 = i + 1
            break
        except KeyError:
            # Key is not present so add to dict
            remainder_arr[remainder] = i + 1
            pass
    return (index_1, index_2)


'''
Given an array of integers and a target value, determine the number of pairs of array elements that have a
difference equal to the target value.
Ex. [1, 2, 4, 3] and a target value of 1 would return 3 since 2 - 1 = 1, 3 - 2 = 1, 4 - 3 = 1
'''
def num_of_pairs(k, arr):
    '''

    :param k: The difference value
    :param arr: an unsorted array
    :return: An ordered pair of indexes from the cost array (starting at 1)
    '''
    # ANDing the two sets together reveals the number of difference pairs
    return len(set(arr) & set(x + k for x in arr))


'''
Sock Merchant

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array
of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
Ex. [1, 2, 1, 2, 1, 3, 2] would return 2
'''
def sock_merchant(arr):
    '''
    Finds the total number of paired identical numbers in an unsorted array
    :param arr: An unsorted array
    :return: Number of identical pairs
    '''
    # Data Validation on param
    error_message = 'Parameter must be a populated integer array'
    if not isinstance(arr, list):
        raise TypeError(error_message)
    if not arr:
        raise ValueError(error_message)

    # Sorting O(n log n)
    arr.sort()

    num_pairs = 0
    pair_ahead_flag = False

    # Iterating through every other element O(n/2)
    for i in range(0, len(arr), 2):
        # Look at the element before the current
        if not pair_ahead_flag and i-1 >= 0 and arr[i] == arr[i-1]:
            num_pairs += 1
            continue
        # Look at the element ahead of the current
        elif i+1 != len(arr) and arr[i] == arr[i+1]:
            num_pairs += 1
            pair_ahead_flag = True
            continue
        else:
            pair_ahead_flag = False

    # This one liner works, but is not as fast as the above solution
    # return (sum(arr.count(x)//2 for x in set(arr)))
    return num_pairs


'''
Counting Valleys

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,
step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.
We define the following terms:
    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and
    ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and
    ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
Ex. "DDUUUUDD" would return 1
'''
def counting_valleys(s):
    '''
    Prints the total number of valleys where a valley is defined as
    one or more steps below sea level and then back to sea level
    :param s: A string containg only U's and D's
    :return: The number of valleys
    '''
    # Data Validation on param
    error_message = 'Parameter must be a string of non zero length.'
    if not isinstance(s, str):
        raise TypeError(error_message)
    if not s:
        raise ValueError(error_message)

    # Setting the current level to sea level (i.e. 0)
    current_level = 0
    num_valleys = 0

    for c in s.upper():
        if c is 'U':
            current_level += 1
            if current_level == 0:
                num_valleys += 1
        elif c is 'D':
            current_level -= 1
        else:
            raise ValueError(error_message)

    return num_valleys

'''
Jumping on the Clouds

Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads
and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current
cloud plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump
from her starting postion to the last cloud. It is always possible to win the game.
Ex. c = [0, 1, 0, 0, 0, 1, 0] would return 3
'''
def jumping_on_clouds(c):
    '''
    Finds the most efficient path with the least amount of cloud jumps. Jumps can be 1 or 2 higher than the current cloud.
    :param c: A list formatted in binary, where 1's have to be avoided (thunderheads)
    :return: the minimum jumps possible. Returns -1 otherwise
    '''
    # Data Validation on param
    error_message = 'Parameter must be a binary list.'
    if not isinstance(c, list):
        raise TypeError(error_message)
    if not c:
        raise ValueError(error_message)

    num_jumps = -1
    i = 0
    while(i < len(c)):
        num_jumps += 1
        if c[i] == 1 and i < (len(c) - 1) and c[i + 1] == 1: 
            num_jumps = -1
            break
        # Attempts to jump by 2
        if i < (len(c) - 2) and c[i + 2] == 0:
            i += 1
        i += 1

    return num_jumps


'''
Repeated String

Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string
Ex. s = 'aba', n = 10. output 7
'''
def repeated_string(s, n):
    '''
    Gets the number of a's in an infinite repeating string s of length n
    :param s: String to be repeated
    :param n: Integer of the length of the repeating string
    :return: Returns the number of a's in the repeated string
    '''
    # Data Validation on params
    error_message = 'Parameters must be a string of non zero length and an integer.'
    if not isinstance(s, str):
        raise TypeError(error_message)
    if not isinstance(n, int):
        raise TypeError(error_message)
    if not s:
        raise ValueError(error_message)

    # Finds the nubmer of a's in the string
    # Counting O(n)
    num_a_in_s = s.count("a")
    # Multiplies that by the number of whole strings in length n
    total_num_a = int(n/len(s)) * num_a_in_s
    # Finds the remainding a's in the string
    total_num_a += s[:(n - (int(n/len(s)) * len(s)))].count("a")

    return total_num_a

'''
Fraudulent Activity Notifications

HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending
for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send
the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print
the number of times the client will receive a notification over all n days
Ex. expenditures = [10, 20, 30, 40, 50], d = 3 would return 1
'''
def get_median_sorted(arr):
    '''
    Returns the median from a sorted array of integers
    :param arr: A sorted list of integers
    :return: The median of the list
    '''
    middle = int(len(arr)/2)
    # Even case
    if len(arr)%2 == 0:
        return ((arr[middle - 1] + arr[middle]) / 2)
    else:
        return arr[middle]

def activity_notifications(expenditure, d):
    '''
    Returns the number of notifications that would be sent out to the client. A notification is sent if the current day's
    expenditures is greater than or equal to the median of the preceding days (d) median
    :param expenditure: An list ordered chronologically
    :param d: The number of trailing days
    :return: The number of notifications to be sent
    '''
    trailing_expenditures = []
    # Initialize trailing expenditures
    for i in range(0, d):
        bisect.insort(trailing_expenditures, expenditure[i])

    num_notifications = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= (2 * get_median_sorted(trailing_expenditures)):
            num_notifications += 1
        # Delete the transaction from d days ago
        # The below line works, but it is not as efficient as a binary search removal
        # trailing_expenditures.remove(expenditure[i - d])
        del trailing_expenditures[bisect.bisect_left(trailing_expenditures, expenditure[i - d])]
        bisect.insort(trailing_expenditures, expenditure[i])

    return num_notifications

'''
Merge Sort: Counting Inversions

In an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr [j].
In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an
inversion, we can swap adjacent elements.

Given d datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

Ex. arr = [1, 1, 1, 2, 2] would return 0  
Ex. arr = [2, 1, 3, 1, 2] would return 4
'''
def merge_halves(left, right):
    result = []
    i, j, swaps = 0, 0, 0
    len_left = len(left)
    len_right = len(right)
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            swaps += (len_left - i)
    '''
    # Either would work
    if len_left == i:
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    '''
    result += left[i:]
    result += right[j:]
    return swaps, result

def merge_sort(arr):
    '''
    Sorts the left and half side until each side has 1 element, then merges those sides back together recursively
    '''
    n = len(arr)
    if n < 2:
        return 0, arr[:]
    else:
        middle = int(n / 2)
        left_swaps, left = merge_sort(arr[:middle])
        right_swaps, right = merge_sort(arr[middle:])
        m_swaps, result = merge_halves(left, right)
        return (left_swaps + right_swaps + m_swaps), result

def count_inversions(arr):
    # Merge sort O(n log n)
    swaps, result = merge_sort(arr)
    return swaps

'''
Strings: Making Anagrams

We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second
string. In other words, both strings must contain the same exact letters in the same exact frequency. For example,
bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of
each other if the first string's letters can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams,
but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number
of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
'''
def making_anagrams(str_1, str_2):
    '''
    Returns the number of deleted characters from both strings in order to be left with an anagram.
    We consider two strings to be anagrams of each other if the first string's letters can be rearranged
    to form the second string. In other words, both strings must contain the same exact letters in
    the same exact frequency.
    :param str_1: A string of alphabetical characters
    :param str_2 A string of alphabetical characters
    :return: The number of deletions required. 0 if not possible
    '''
    # Data Validation
    if not (isinstance(str_1, str) and isinstance(str_2, str)):
        raise TypeError('Parameters must be strings contianing alphabetical characters')

    # Sorted O(n log n)
    str_1_sorted = sorted(str_1)
    str_2_sorted = sorted(str_2)
    str_1_ptr, str_2_ptr, num_deletions = 0, 0, 0
    len_str_1, len_str_2 = len(str_1_sorted), len(str_2_sorted)
    
    while(str_1_ptr < len_str_1 and str_2_ptr < len_str_2):
        # If both strings contain the character, then it belongs in the anagram
        if str_1_sorted[str_1_ptr] == str_2_sorted[str_2_ptr]:
            str_1_ptr += 1
            str_2_ptr += 1
        # Enters if str_1's element comes alphabetically before str_2's element
        elif str_1_sorted[str_1_ptr] < str_2_sorted[str_2_ptr]:
            num_deletions += 1
            str_1_ptr += 1
        else:
            num_deletions += 1
            str_2_ptr += 1

    #print("str_1_ptr: {} len_str_1: {}".format(str_1_ptr, len_str_1))
    #print("str_2_ptr: {} len_str_2: {}".format(str_2_ptr, len_str_2))

    num_deletions += (len_str_1 - str_1_ptr) + (len_str_2 - str_2_ptr)

    return num_deletions


'''
Alternating Characters

You are given a string containing characters A and B only. Your task is to change it into a string such that there
are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s = 'AABAAB', remove an A at positions 0 and 3 to make s = ' ABAB' in 2 deletions.
Ex.
AAAA -> 3
BBBBB -> 4
ABABABAB -> 0
BABABA -> 0
AAABBB -> 4
'''
def alternating_characters(s):
    '''
    Finds the number of deleted characters necessary such that s is left alternating between 'A' and 'B'
    :param s: A string containing only A's and B's
    :return: Number of deletions
    '''
    # Data Valiation
    error_message = 'Parameter must be a string containing only A\'s and B\'s'
    if not isinstance(s, str):
        raise TypeError(error_message)
    num_of_deletions = 0

    for i in range(0, len(s) - 1):
        if not (s[i].upper() == "A" or s[i].upper() == "B"):
            raise ValueError(error_message)
        if s[i].upper() == s[i + 1].upper():
            num_of_deletions += 1

    return num_of_deletions


'''
Sherlock and the Valid String

Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters
will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

For example, if s = 'abc', it is a valid string because frequencies are {a : 1, b : 1, c : 1}. So is s = 'abcc' because we
can remove one c and have 1 of each character in the remaining string.

Ex. 'xxxaabbccrry' -> NO
'aabbcd' -> NO
'aabbc' -> YES
'''
def is_valid(s):
    '''
    Checks if all the charaters occur the same number of times. One extra character is allowed to be present.
    :param s: A string of letters
    :return: 'YES' if valid, 'NO' otherwise
    '''
    # Data Validation
    if not isinstance(s, str):
        raise TypeError('Parameter must be a string of letters.')

    # Sorted O(n log n)
    s_sorted = sorted(s)
    last_char_freq, current_char_freq, i = 1, 1, 0

    while (i < (len(s) - 1) and s_sorted[i] == s_sorted[i + 1]):
        last_char_freq += 1
        i += 1
    
    output_str = 'YES'
    # Accounts for the case where the string is comprised of one character
    if last_char_freq == len(s):
        return output_str
    
    extra_char_available = True
    for i in range(i + 1, len(s_sorted) - 1):
        # Accounts for the next char equaling the current and the one after that being different (i.e. an extra character)
        if (s_sorted[i] == s_sorted[i + 1]):
            current_char_freq += 1
            i += 1
            continue
        # Else means the following since it's sorted
        # elif (s_sorted[i] < s_sorted[i + 1]):
        else:
            if current_char_freq == 1 and not last_char_freq == 1:
                extra_char_available = False
            elif current_char_freq < last_char_freq:
                output_str = 'NO'
                break
            
        if current_char_freq > last_char_freq:
            if extra_char_available:
                extra_char_available = False
            else:
                output_str = 'NO'
                break
        
        current_char_freq = 1
        i += 1

    if output_str == 'YES' and current_char_freq == 1 and (not last_char_freq == 1) and not extra_char_available:
        output_str = 'NO'
    elif current_char_freq > last_char_freq:
        output_str = 'NO'

    return output_str



'''
Special String Again

A string is said to be a special palindromic string if either of two conditions is met:
    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.
A special palindromic substring is any substring of a string which meets one of those criteria. Given a string,
determine how many special palindromic substrings can be formed from it.
Ex. s = 'abcbaba' n = 7 result is 10
{a, b, c, b, a, b, a, bcb, bab, aba}
'''
def substr_count(n, s):
    # Data Validation
    if not isinstance(s, str):
        raise TypeError('Parameter must be a string of letters.')
    if n != len(s):
        raise ValueError('Parameter n must be the lenght of the string.')

    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                # Accounts for the special case os xx.xx where the middle character is indifferent
                if s[x:y] == s[y+1 : 2*y-x+1]:
                    count += 1
                break
    return count


'''
Hash Tables: Ransom Note

A man desires to make a ransom not from a magazine. Don't ask me why.
Given the words in the magazine and the words in the ransom note, return true if he can replicate his
ransom note exactly using whole words from the magazine; otherwise, return false
The words in his note are case-sensitive and he must use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.
Ex. magazine = 'give me one grand today night' note = 'give one grand today' result 'Yes'
Ex. magazine = 'Give me one grand today night' note = 'give one grand today' result 'No'
'''
def check_magazine(magazine, ransom):
    '''
    Returns true if the magazine contains all the words (case sensitive) found in the ransom note
    without having to use substrings or concatentation of characters
    :param magazine: An array of strings from a magazine
    :param ransom: An array of strings desired to make the ransom note
    :return: A boolean; true if all the ransom strings are in the magazine strings
    '''
    # Creates a dictionary of the ransom note's words and their number of occurences
    # Then subtracts out the magazine. If the result is an empty dictionary, then the
    # ransom note can be made from the magazine
    # Counter O(n)
    return (Counter(ransom) - Counter(magazine)) == {}


'''
Two Strings

Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring.
Ex. s1 = 'hello', s2 = 'world' would print 'YES'
Ex. s1 = 'hi', s2 = 'world' would print 'NO'
'''
def two_strings(s1, s2):
    '''
    Finds if 2 strings share a common substring where a substring can be as small as a one character.
    :param s1: A string
    :param s2: A string
    :retrun: 'YES' if they share a common substring, 'NO' otherwise
    '''
    # Data Validation
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError('Parameters must be strings.')

    # Counter O(n)
    s1_dict = Counter(s1)
    output_str = 'NO'
    for c in s2:
        if c in s1_dict:
            output_str = 'YES'
            break
    return output_str


'''
Sherlock and Anagrams

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
Ex. "mom" -> all anagrammatic pairs are ["m", "m"] and ["mo", "om"] at positions [0, 2] and [[0:1], [1:2]] respectively
'''
def sherlock_and_anagrams(s):
    '''
    Returns the number of anagrams present in the given string
    :param s: A string to search for anagrams
    :return: The maximum number of anagrams possible
    '''
    # Data Validation
    if not isinstance(s, str):
        raise TypeError('Parameter must be a string of letters.')

    # The key is anagrams are identical after sorting alphabetically
    anagrams = 0
    substrings = {i: [] for i in range(1, len(s) + 1)}
    for j in range(len(s)):
        for i in range(j + 1, len(s) + 1):
            # Sorted O(n log n)
            substr = ''.join(sorted(s[j:i]))
            # Sort substrings into dict by length
            for k in range(0, len(substrings[i - j])):
                if substrings[i - j][k] == substr:
                    anagrams += 1
            substrings[i - j].append(substr)
    return anagrams


'''
Count Triplets

You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those
indices are in geometric progression for a given common ratio r and i < j < k.
Ex. a, ar, ar^1, ar^2, ar^3,...
'''
def count_triplets(arr, r):
    '''
    Returns the number of triplets that are in a geometric progression present in an array
    :param arr: A sorted array
    :param r: The common ratio (multiplier) that defines the pattern
    :return: The maximum number of triplets that follow geometric progression
    '''
    # Data Validation on param
    if not isinstance(arr, list):
        raise TypeError('Parameter must be a populated sorted integer array')
    if not isinstance(r, int):
        raise TypeError('The common ratio (multiplier) parameter must be a positive integer.')
    if not r >= 0:
        raise ValueError('The common ratio (multiplier) parameter must be a positive integer.')

    # Stores number of tuples with two elements that can be formed if the key is present
    potential_two_tuples = defaultdict(int)
    # Stores number of tuples with three elements that can be formed if the key is present
    potential_three_tuples = defaultdict(int)
    count = 0
    for k in arr:
        # k completes the three tuples assuming k/(r^2) and k/r exist
        count += potential_three_tuples[k]
        # For any element of array, a three element tuple can be formed from k*r given k / r is already found
        # Also k forms the second element
        potential_three_tuples[k * r] += potential_two_tuples[k]
        # For any element of array, a two element tuple can be formed from k*r
        # Also k forms the first element
        potential_two_tuples[k * r] += 1
    return count


'''
Frequency Queries

You are given q queries. Each query is of the form two integers described below: 
- 1 x: Insert x in your data structure. 
- 2 y: Delete one occurence of y from your data structure, if present. 
- 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
Ex.
Operation   Array               Output
[1, 5]      [5]
[1, 6]      [5, 6]
[3, 2]                          0
[1, 10]     [5, 6, 10]
[1, 10]     [5, 6, 10, 10]
[1, 6]      [5, 6, 6, 10, 10]
[2, 5]      [6, 6, 10, 10]
[3, 2]                          1
'''
def freq_query(queries):
    '''
    From a 2D array, perform the following queries
    1: Insert x in your data structure. 
    2: Delete one occurence of y from your data structure, if present. 
    3: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
    :param queries: A 2D array containg 2 integers
    :return: An array contianing the results from any '3' operations
    '''
    # Data Validation
    error_message = 'The parameter must be a 2D list containing operations and values.'
    if not isinstance(queries, list):
        raise TypeError(error_message)
    if not queries:
        raise ValueError(error_message)

    output_arr = []
    # Counter O(n)
    by_value = Counter()
    by_freq = Counter()
    for query in queries:
        operation, value = query[0], query[1]
        if operation == 1:
            by_freq[by_value[value]] -= 1
            by_value[value] += 1
            by_freq[by_value[value]] += 1
        elif operation == 2:
            if by_value[value] > 0:
                by_freq[by_value[value]] -= 1
                by_value[value] -= 1
                by_freq[by_value[value]] += 1
        elif operation == 3:
            output_arr.append(0)
            if by_freq[value] > 0:
                output_arr[-1] = 1
        else:
            raise ValueError('1, 2, and 3 are the only valid operations.')

    return output_arr
