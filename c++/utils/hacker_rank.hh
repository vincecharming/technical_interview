//
// Vincent Charming (c) 2019
//

#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#include <bits/stdc++.h>

namespace hacker_rank
{
///
/// Returns the number of common elemnts found in 2 distinct sorted arrays
/// The arrays are assumed to be sorted
///
int get_num_common_in_array(const int *arr_1, const int *arr_2);

///
/// Add 1 to a number stored with each digit in an element of an array
/// Ex. [6, 8, 1] > [6, 8, 2]
///
std::vector<int> add_one_to_array_num(const std::vector<int> &vect);

///
/// Arrays -> 2D Array - DS
///
/// Find the largest sum of an hourglass pattern as defined below
/// a b c
///   d
/// e f g
/// Ex. Function returns 7 for the matrix below
/// 1 1 1 0 0 0
/// 0 1 0 0 0 0
/// 1 1 1 0 0 0
/// 0 0 0 0 0 0
/// 0 0 0 0 0 0
/// 0 0 0 0 0 0
///
int hourglass_sum(std::vector<std::vector<int>> arr);

///
/// Arrays -> Arrays: Left Rotation
///
/// Given an array of integers and a number, perform that number of left rotations on the array
/// Return the updated array
///
std::vector<int> rot_left(std::vector<int> arr, int d);

///
/// Arrays -> Minimum Swaps 2
///
/// Given an unordered array consisting of consecutive integers without any duplicates.
/// You are allowed to swap any two elements.
/// You need to find the minimum number of swaps required to sort the array in ascending order.
///
int minimum_swaps(std::vector<int> arr);

///
/// Arrays -> Array Manipulation
///
/// Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to
/// each of the array element between two given indices, inclusive. Once all operations have been performed,
/// return the maximum value in your array.
/// Ex. Add the values of k between the indicies a and b inclusive. n = 10
///     a b k
///     1 5 3
///     4 8 7
///     6 9 1
///     index-> 1 2 3  4  5 6 7 8 9 10
///            [0,0,0, 0, 0,0,0,0,0, 0]
///            [3,3,3, 3, 3,0,0,0,0, 0]
///            [3,3,3,10,10,7,7,7,0, 0]
///            [3,3,3,10,10,8,8,8,1, 0] return 10 because it is the largets value after all operations
///
int64_t array_manipulation(int n, std::vector<std::vector<int>> queries);

///
/// Arrays -> New Year Chaos
///
/// Initial positions increment by 1 from front of the back of the line (n).
/// Any person in the queue can bribe the person directly in front of them to swap positions.
/// If two people swap positions, they still wear the same sticker denoting their original places in line.
/// One person can bribe at most two others. Return the minimum number of bribes (swaps) possible.
/// Throw an error if the line is too chaotic (i.e. not a possible configuration given the parameters)
/// Ex. 2 1 5 3 4 would return 3 since:
/// 1 2 3 4 5 Start
/// 2 1 3 4 5 1 Swap
/// 2 1 3 5 4 2 Swaps
/// 2 1 5 3 4 3 Swaps
/// Ex. 2 5 1 3 4 would throw an error since this is too chaotic
///
int minimum_bribes(std::vector<int> arr);

///
/// Given the words in the magazine and the words in the ransom note, return true if he can replicate his
/// ransom note exactly using whole words from the magazine; otherwise, return false
/// The words in his note are case-sensitive and he must use only whole words available in the magazine.
/// He cannot use substrings or concatenation to create the words he needs.
///
bool check_magazine(std::vector<std::string> magazine, std::vector<std::string> ransom);

///
/// Given two strings, determine if they share a common substring. A substring may be as small as one character.
/// Ex. the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
///
bool two_string_common_char(std::string s1, std::string s2);

/// 
/// Frequency Queries
/// You are given  queries. Each query is of the form two integers described below:
/// 1 x : Insert x in your data structure.
/// 2 y : Delete one occurence of y from your data structure, if present.
/// 3 z : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
///
std::vector<int> freq_query(std::vector<std::vector<int>> queries);

///
/// Given an unordered list of intervals, simplify into the least number of intervals by combining
/// common intervals.
/// Ex. [(0, 7), (5, 10)] -> [(0, 10)]
///
std::vector<std::pair<int, int>> get_overlapping_intervals(std::vector<std::pair<int, int>> arr);

} // namespace hacker_rank
