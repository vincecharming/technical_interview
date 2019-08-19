"""
Vincent Charming (c) 2019
Tests for HackerRank Sample Problems
Note: Normally larger data sets would be imported from a YAML config file to test time complexity
"""

import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import utils.hacker_rank as hacker_rank

__author__ = 'vcharming'


class TestHackerRank(unittest.TestCase):

    def test_get_num_common_in_array(self):
        test_arrays_and_results = [
            (([1, 2, 5, 7, 8, 11, 15], [0, 4, 5, 6, 9, 10, 16]), 1),
            (([0, 5, 5, 5, 8, 14, 21], [0, 4, 5, 6, 9, 10, 16]), 2),
            (([0, 2, 5, 7, 8, 10, 15], [0, 4, 5, 6, 9, 10, 16]), 3),
            (([4, 8, 11, 321], [0, 4, 5]), 1)]
        for test_arrays, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.get_num_common_in_array(test_arrays[0], test_arrays[1]), result)
        # Showcasing 2 different ways to invoke this test
        with self.assertRaises(TypeError):
            hacker_rank.get_num_common_in_array("foo", "bar")
        self.assertRaises(TypeError, lambda: hacker_rank.get_num_common_in_array(True, None))
        self.assertRaises(ValueError, lambda: hacker_rank.get_num_common_in_array([], [0, 4, 5, 6, 9, 10, 16]))

    def test_add_one_to_array_num(self):
        test_arrays_and_results = [
            ([5], [6]),
            ([2, 8, 4], [2, 8, 5]),
            ([7, 2, 0], [7, 2, 1]),
            ([3, 1, 9], [3, 2, 0]),
            ([9, 9, 9], [1, 0, 0, 0])]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.add_one_to_array_num(test_array), result)
        self.assertRaises(TypeError, lambda: hacker_rank.add_one_to_array_num(None))
        self.assertRaises(ValueError, lambda: hacker_rank.add_one_to_array_num([]))

    def test_hourglass_sum(self):
        test_arrays_and_results = [
            ([[1, 1, 1],
              [0, 1, 0],
              [1, 1, 1]], 7),
            ([[1, 1, 1, 0, 9, 7],
              [0, 2, 0, 0, 8, 9],
              [1, 1, 1, 0, 0, 0],
              [0, 9, 0, 3, 2, 1],
              [9, 0, 2, 6, 8, 0],
              [0, 0, 1, 1, 4, 8]], 27),
            ([[-9, -9, -4, 1, 1, 1],
              [0, -2, 0, 4, 3, 2],
              [-1, -9, -9, 1, 2, 3],
              [0, 0, 8, 6, 6, 0],
              [0, 0, 0, -2, 0, 0],
              [0, 0, 1, 2, 4, 0]], 28)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.hourglass_sum(test_array), result)
        self.assertRaises(ValueError, lambda: hacker_rank.hourglass_sum([[1, 0], [0, 1]]))

    def test_what_flavors(self):
        test_arrays_and_results = [
            (([1, 4, 5, 3, 2], 4), (1, 4)),
            (([3, 4, 5, 1, 2], 4), (1, 4)),
            (([2, 2, 4, 5], 4), (1, 2))]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.what_flavors(test_array[0], test_array[1]), result)

    def test_num_of_pairs(self):
        test_arrays_and_results = [
            ((2, [1, 5, 3, 4, 2]), 3),
            ((1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912]), 0),
            ((2, [1, 3, 5, 8, 6, 4, 2]), 5)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.num_of_pairs(test_array[0], test_array[1]), result)

    def test_sock_merchant(self):
        test_arrays_and_results = [
            ([1, 2, 1, 2, 1, 3, 2], 2),
            ([1, 14, 1, 14, 0, 14, 2, 0], 3),
            ([0, 0, 0, 0, 1, 0, 1], 3),
            ([1, 2, 8, 5, 9, 0, 4], 0)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.sock_merchant(test_array), result)
        self.assertRaises(TypeError, lambda: hacker_rank.sock_merchant("foo"))
        self.assertRaises(ValueError, lambda: hacker_rank.sock_merchant([]))

    def test_counting_valleys(self):
        test_strings_and_results = [
            ("DDUUUUDD", 1),
            ("UDUDUDUD", 0),
            ("UDDUUDDUUDDUUD", 3),
            ("UUUUUUUUDDDDDD", 0),
            ("UUUUDDDDDDUUUUUUUUU", 1)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.counting_valleys(test_string), result)
        self.assertRaises(TypeError, lambda: hacker_rank.counting_valleys(["foo"]))
        self.assertRaises(ValueError, lambda: hacker_rank.counting_valleys(""))
        self.assertRaises(ValueError, lambda: hacker_rank.counting_valleys("DDUUMUUDD"))

    def test_jumping_on_clouds(self):
        test_arrays_and_results = [
            ([0, 1, 0, 0, 0, 1, 0], 3),
            ([0, 0, 1, 0, 0, 1, 0], 4),
            ([0, 0, 1, 1, 0, 0, 0], -1),
            ([0, 0, 1, 1], -1)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.jumping_on_clouds(test_array), result)
        self.assertRaises(TypeError, lambda: hacker_rank.jumping_on_clouds(0))
        self.assertRaises(ValueError, lambda: hacker_rank.jumping_on_clouds([]))

    def test_repeated_string(self):
        test_strings_and_results = [
            (("aba", 10), 7),
            (("a", 10), 10),
            (("aaaaaa", 10), 10),
            (("aaaaa", 1), 1),
            (("zzzz", 15), 0)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.repeated_string(test_string[0], test_string[1]), result)
        self.assertRaises(TypeError, lambda: hacker_rank.repeated_string(["foo"], 10))
        self.assertRaises(TypeError, lambda: hacker_rank.repeated_string("foo", "10"))
        self.assertRaises(ValueError, lambda: hacker_rank.repeated_string("", 10))

    def test_get_median_sorted(self):
        test_arrays_and_results = [
            ([1, 2, 3, 4, 5], 3),
            ([0, 1, 2, 3, 4, 5], 2.5),
            ([5, 5, 5, 8, 11], 5),
            ([8, 10, 20, 50], 15)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.get_median_sorted(test_array), result)

    def test_activity_notifications(self):
        test_arrays_and_results = [
            (([10, 20, 30, 40, 50], 3), 1),
            (([2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2),
            (([1, 2, 3, 4, 4], 4), 0),
            (([10, 20, 30, 40, 50], 3), 1)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.activity_notifications(test_array[0], test_array[1]), result)

    def test_count_inversions(self):
        test_arrays_and_results = [
            ([1, 1, 1, 2, 2], 0),
            ([2, 1, 3, 1, 2], 4),
            ([1, 5, 3, 7], 1),
            ([7, 5, 3, 1], 6),
            ([1, 3, 5, 7], 0),
            ([3, 2, 1], 3)]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.count_inversions(test_array), result)

    def test_making_anagrams(self):
        test_strings_and_results = [
            (("cde", "abc"), 4),
            (("abbze", "abbze"), 0),
            (("abbze", "bazeb"), 0),
            (("absdjkvuahdakejfnfauhdsaavasdlkj", "djfladfhiawasdkjvalskufhafablsdkashlahdfa"), 19)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.making_anagrams(test_string[0], test_string[1]), result)
        self.assertRaises(TypeError, lambda: hacker_rank.making_anagrams(["foo"], "bar"))
        self.assertRaises(TypeError, lambda: hacker_rank.making_anagrams("foo", ["bar"]))

    def test_alternating_characters(self):
        test_strings_and_results = [
            ("AAAA", 3),
            ("BBBBB", 4),
            ("ABABABAB", 0),
            ("BABABA", 0),
            ("AAABBB", 4),
            ("AAABBBAABB", 6),
            ("AABBAABB", 4),
            ("ABABABAA", 1)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.alternating_characters(test_string), result)
        self.assertRaises(TypeError, lambda: hacker_rank.alternating_characters(["AAAA"]))
        self.assertRaises(ValueError, lambda: hacker_rank.alternating_characters("AAZZBB"))

    def test_is_valid(self):
        test_strings_and_results = [
            ("aabbcd", "NO"),
            ("aabbc", "YES"),
            ("aabbccddeefghi", "NO"),
            ("abcdefghhgfedecba", "YES"),
            ("a", "YES"),
            ("aaaabbcc", "NO")]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.is_valid(test_string), result)
        self.assertRaises(TypeError, lambda: hacker_rank.is_valid(["aabbcd"]))

    def test_substr_count(self):
        test_strings_and_results = [
            ((7, "abcbaba"), 10),
            ((5, "asasd"), 7),
            ((4, "aaaa"), 10),
            ((5, "aakaa"), 9)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.substr_count(test_string[0], test_string[1]), result)
        self.assertRaises(TypeError, lambda: hacker_rank.substr_count(3, ["foo"]))
        self.assertRaises(ValueError, lambda: hacker_rank.substr_count(4, "foo"))

    def test_check_magazine(self):
        test_arrays_and_results = [
            ([["give", "me", "one", "grand", "today", "night"], ["give", "one", "grand", "today"]], True),
            ([["two", "times", "three", "is", "not", "four"], ["two", "times", "two", "is", "four"]], False),
            ([["ive", "got", "a", "lovely", "bunch", "of", "coconuts"], ["ive", "got", "coconuts", "a"]], True),
            ([["ive", "got", "a", "lovely", "bunch", "of", "coconuts"], ["ive", "got", "CoCoNuTs", "a"]], False),
            ([["ive", "got", "a", "lovely", "bunch", "of", "coconuts"], ["ive", "got", "some", "coconuts"]], False)]
        for test_arrays, result in test_arrays_and_results:
            if result:
                self.assertTrue(hacker_rank.check_magazine(test_arrays[0], test_arrays[1]))
            else:
                self.assertFalse(hacker_rank.check_magazine(test_arrays[0], test_arrays[1]))

    def test_two_strings(self):
        test_strings_and_results = [
            (("hello", "world"), "YES"),
            (("hi", "world"), "NO"),
            (("wouldyoulikefries", "abcabcabcabcabcabc"), "NO"),
            (("hackerrankcommunity", "cdecdecdecde"), "YES"),
            (("jackandjill", "wentupthehill"), "YES"),
            (("writetoyourparents", "fghmqzldbc"), "NO")]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.two_strings(test_string[0], test_string[1]), result)
        self.assertRaises(TypeError, lambda: hacker_rank.two_strings(["foo"], "bar"))
        self.assertRaises(TypeError, lambda: hacker_rank.two_strings("foo", ["bar"]))

    def test_sherlock_and_anagrams(self):
        test_strings_and_results = [
            ("abcd", 0),
            ("ifailuhkqq", 3),
            ("hucpoltgty", 2),
            ("azbz", 2),
            ("kkkk", 10),
            ("mqkidziqkmd", 20)]
        for test_string, result in test_strings_and_results:
            self.assertEqual(hacker_rank.sherlock_and_anagrams(test_string), result)
        self.assertRaises(TypeError, lambda: hacker_rank.sherlock_and_anagrams(["foo"]))

    def test_count_triplets(self):
        test_dicts = [
            {"r": 2, "arr": [1, 2, 2, 4], "result": 2},
            {"r": 5, "arr": [1, 5, 5, 25, 25, 25, 25], "result": 8},
            {"r": 5, "arr": [1, 5, 5, 25, 125], "result": 4},
            {"r": 0, "arr": [1, 5, 5, 25, 125], "result": 0},
            {"r": 4, "arr": [1, 4, 16, 348], "result": 1}]
        for test_dict in test_dicts:
            self.assertEqual(hacker_rank.count_triplets(test_dict["arr"], test_dict["r"]), test_dict["result"])
        self.assertRaises(TypeError, lambda: hacker_rank.count_triplets(34508, 2))
        self.assertRaises(TypeError, lambda: hacker_rank.count_triplets([1, 2, 2, 4], [2]))
        self.assertRaises(ValueError, lambda: hacker_rank.count_triplets([1, 2, 2, 4], -1))

    def test_freq_query(self):
        test_arrays_and_results = [
            ([[1, 5],
              [1, 6],
              [3, 2],
              [1, 10],
              [1, 10],
              [1, 6],
              [2, 5],
              [3, 2]], [0, 1]),
            ([[3, 4],
              [2, 1003],
              [1, 16],
              [3, 1]], [0, 1]),
            ([[1, 3],
              [2, 3],
              [3, 2],
              [1, 4],
              [1, 5],
              [1, 5],
              [1, 4],
              [3, 2],
              [2, 4],
              [3, 2]], [0, 1, 1])]
        for test_array, result in test_arrays_and_results:
            self.assertEqual(hacker_rank.freq_query(test_array), result)
        self.assertRaises(TypeError, lambda: hacker_rank.freq_query(0))
        self.assertRaises(ValueError, lambda: hacker_rank.freq_query([]))


def suite():
    functions_suite = unittest.TestLoader().loadTestsFromTestCase(TestHackerRank)
    return unittest.TestSuite([functions_suite])


if __name__ == "__main__":
    text_test_result = unittest.TextTestRunner(verbosity=1).run(suite())
    sys.exit(0 if text_test_result.wasSuccessful() else 1)
