//
// Vincent Charming (c) 2019
//

#include "hacker_rank.hh"

#include "gtest/gtest.h"

namespace hacker_rank
{

//
// ############################################################################
//

TEST(test_get_num_common_in_array, parse_status)
{
    const int test_arrays[8][7] = {{1, 2, 3, 7, 8, 11, 15},
                                   {0, 4, 5, 6, 9, 10, 16}, // 0
                                   {1, 2, 5, 7, 8, 11, 15},
                                   {0, 4, 5, 6, 9, 10, 16}, // 1
                                   {0, 5, 5, 5, 8, 14, 21},
                                   {0, 4, 5, 6, 9, 10, 16}, // 2
                                   {0, 2, 5, 7, 8, 10, 15},
                                   {0, 4, 5, 6, 9, 10, 16}}; // 3


    int test_answer = 0;
    for (int j = 0; j < (sizeof(test_arrays) / sizeof(test_arrays[0])) - 1; j += 2)
    {
        if (j != 0)
        {
            test_answer = j / 2;
        }
        EXPECT_EQ(get_num_common_in_array(test_arrays[j], test_arrays[j + 1]), test_answer);
    }
}

//
// ############################################################################
//

TEST(test_add_one_to_array_num, parse_status)
{
    std::vector<int> test_vectors[10]
        = {{5}, {6}, {2, 8, 4}, {2, 8, 5}, {7, 2, 0}, {7, 2, 1}, {3, 1, 9}, {3, 2, 0}, {9, 9, 9}, {1, 0, 0, 0}};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0]) - 1); j += 2)
    {
        std::vector<int> expected_output = add_one_to_array_num(test_vectors[j]);
        std::vector<int> output          = test_vectors[j + 1];
        for (int i = 0; i < expected_output.size(); i++)
        {
            EXPECT_EQ(expected_output[i], output[i]);
        }
    }
}

//
// ############################################################################
//

TEST(test_hourglass_sum, parse_status)
{
    const std::vector<std::vector<int>> test_hourglass[3] = {{{1, 1, 1},
                                                              {0, 1, 0},
                                                              {1, 1, 1}},
                                                             {{1, 1, 1, 0, 9, 7},
                                                              {0, 2, 0, 0, 8, 9},
                                                              {1, 1, 1, 0, 0, 0},
                                                              {0, 9, 0, 3, 2, 1},
                                                              {9, 0, 2, 6, 8, 0},
                                                              {0, 0, 1, 1, 4, 8}},
                                                             {{-9, -9, -4,  1,  1,  1},
                                                              { 0, -2,  0,  4,  3,  2},
                                                              {-1, -9, -9,  1,  2,  3},
                                                              { 0,  0,  8,  6,  6,  0},
                                                              { 0,  0,  0, -2,  0,  0},
                                                              { 0,  0,  1,  2,  4,  0}}};
    const int                           expected_sums[3]  = {7, 27, 28};

    for (int j = 0; j < (sizeof(test_hourglass) / sizeof(test_hourglass[0])); j++)
    {
        EXPECT_EQ(hourglass_sum(test_hourglass[j]), expected_sums[j]);
    }

    // Test that the matrix must be at least 3x3
    EXPECT_THROW(hourglass_sum({{1, 0}, {0, 1}}), std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_rot_left, parse_status)
{
    const std::vector<std::vector<int>> test_vectors[4] = {{{1, 2, 3}, {2}, {3, 1, 2}},
                                                           {{1, 2, 3}, {5}, {3, 1, 2}},
                                                           {{0, -9, 4, 3, 2, 1}, {3}, {3, 2, 1, 0, -9, 4}},
                                                           {{8, -15, 21, 1}, {0}, {8, -15, 21, 1}}};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(rot_left(test_vectors[j][0], test_vectors[j][1][0]), test_vectors[j][2]);
    }

    // Test that the rotation number must be positive
    EXPECT_THROW(rot_left({1, 0, 8}, -1), std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_minimum_swaps, parse_status)
{
    const std::vector<std::vector<int>> test_vectors[2] = {{{1}, {3, 2, 1}},
                                                           {{3}, {4, 3, 1, 2}}};
    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(minimum_swaps(test_vectors[j][1]), test_vectors[j][0][0]);
    }

    // Test that the vector cannot be less than 2 for swapping
    EXPECT_THROW(minimum_swaps({1}), std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_array_manipulation, parse_status)
{
    const std::vector<std::vector<int>> test_vectors[2]
        = {{{1, 2, 100}, {2, 5, 100}, {3, 4, 100}}, {{1, 5, 3}, {4, 8, 7}, {6, 9, 1}}};
    const int n_values[2]     = {5, 10};
    const int expected_max[2] = {200, 10};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(array_manipulation(n_values[j], test_vectors[j]), expected_max[j]);
    }

    // Test that the vector has exactly 3 elements
    EXPECT_THROW(array_manipulation(3, {{1, 2, 100, 5}, {7, 4, 0, 9}}), std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_minimum_bribes, parse_status)
{
    const std::vector<std::vector<int>> test_vectors[4] = {{{1}, {1, 2, 3, 4, 6, 5, 7, 8, 9}},
                                                           {{2}, {1, 2, 3, 6, 4, 5, 7, 8, 9}},
                                                           {{3}, {1, 2, 3, 6, 4, 7, 5, 8, 9}},
                                                           {{7}, {1, 2, 5, 3, 7, 8, 6, 4, 9}}};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(minimum_bribes(test_vectors[j][1]), test_vectors[j][0][0]);
    }

    // Test that the line order is errors when invalid
    EXPECT_THROW(
        {
            try
            {
                minimum_bribes({1, 2, 6, 3, 4, 5, 7, 8, 9});
            }
            catch (std::invalid_argument e)
            {
                // Test that it the correct error message was thrown
                EXPECT_STREQ("Too chaotic", e.what());
                throw;
            }
        },
        std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_check_magazine, parse_status)
{
    const std::vector<std::vector<std::string>> test_vectors[4]
        = {{{"give", "me", "one", "grand", "today", "night"}, {"give", "one", "grand", "today"}},
           {{"two", "times", "three", "is", "not", "four"}, {"two", "times", "two", "is", "four"}},
           {{"ive", "got", "a", "lovely", "bunch", "of", "coconuts"}, {"ive", "got", "some", "coconuts"}},
           {{"ive", "got", "A", "lovely", "bunch", "of", "Coconuts"}, {"ive", "got", "Coconuts", "A"}}};
    const bool expected_output[4] = {true, false, false, true};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(check_magazine(test_vectors[j][0], test_vectors[j][1]), expected_output[j]);
    }
}

//
// ############################################################################
//

TEST(test_two_string_common_char, parse_status)
{
    const std::vector<std::string> test_vectors[4]
        = {{"hello", "world"}, {"hi", "world"}, {"aardvark", "apple"}, {"beetroot", "sandals"}};
    const bool expected_output[4] = {true, false, true, false};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j++)
    {
        EXPECT_EQ(two_string_common_char(test_vectors[j][0], test_vectors[j][1]), expected_output[j]);
    }
}

//
// ############################################################################
//

TEST(test_freq_query, parse_status)
{
    const std::vector<std::vector<int>> test_vectors[6]
        = {{{1, 5}, {1, 6}, {3, 2}, {1, 10}, {1, 10}, {1, 6}, {2, 5}, {3, 2}},
           {{0, 1}},
           {{3, 4}, {2, 1003}, {1, 16}, {3, 1}},
           {{0, 1}},
           {{1, 3},  {1, 38}, {2, 1}, {1, 16}, {2, 1}, {2, 2}, {1, 64}, {1, 84}, {3, 1},  {1, 100},
            {1, 10}, {2, 2},  {2, 1}, {1, 67}, {2, 2}, {3, 1}, {1, 99}, {1, 32}, {1, 58}, {3, 2}},
           {{1, 1, 0}}};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j += 2)
    {
        EXPECT_EQ(freq_query(test_vectors[j]), test_vectors[j + 1][0]);
    }
    // Test that the line order is errors when invalid
    EXPECT_THROW(
        {
            try
            {
                freq_query({{1, 5}, {6, 3}});
            }
            catch (std::invalid_argument e)
            {
                // Test that it the correct error message was thrown
                EXPECT_STREQ("First value in pair must be 1, 2, or 3.", e.what());
                throw;
            }
        },
        std::invalid_argument);
}

//
// ############################################################################
//

TEST(test_get_overlapping_intervals, parse_status)
{
    const std::vector<std::pair<int, int>> test_vectors[2]
        = {{std::make_pair(5, 9),
            std::make_pair(3, 6),
            std::make_pair(8, 12),
            std::make_pair(20, 24),
            std::make_pair(10000, 10010)},
           {std::make_pair(3, 12), std::make_pair(20, 24), std::make_pair(10000, 10010)}};

    for (int j = 0; j < (sizeof(test_vectors) / sizeof(test_vectors[0])); j += 2)
    {
        EXPECT_EQ(get_overlapping_intervals(test_vectors[j]), test_vectors[j + 1]);
    }
    // Test that the line order is errors when invalid
    EXPECT_THROW(
        {
            try
            {
                get_overlapping_intervals({std::make_pair(9, 5), std::make_pair(1, 8)});
            }
            catch (std::invalid_argument e)
            {
                // Test that it the correct error message was thrown
                EXPECT_STREQ("Intervals must be of the following format: (x,y) where y > x", e.what());
                throw;
            }
        },
        std::invalid_argument);
}

} // namespace hacker_rank

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
