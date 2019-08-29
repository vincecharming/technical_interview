//
// Vincent Charming (c) 2019
//

#include "hacker_rank.hh"

namespace hacker_rank
{

int get_num_common_in_array(const int *arr_1, const int *arr_2)
{
    int num_common_elements = 0;
    int arr_2_last_index    = 0;

    for (int i = 0; i < sizeof(arr_1); i++)
    {
        // Skips duplicate values
        if ((i != 0) && (arr_1[i] == arr_1[i - 1]))
        {
            continue;
        }

        // Because the arrays are sorted, we are able to go through the second index incrementally
        for (int j = arr_2_last_index; j < sizeof(arr_2); j++)
        {
            // Skips the remainder of the array that will surely not match the value in question
            if (arr_1[i] < arr_2[j])
            {
                break;
            }
            else
            {
                if (arr_1[i] == arr_2[j])
                {
                    num_common_elements++;
                }
                // Updates the last index, so we can start the next interation further into the array
                arr_2_last_index = j + 1;
            }
        }
    }

    // Return the number of common elemnts
    return num_common_elements;
}

//
// ############################################################################
//

std::vector<int> add_one_to_array_num(const std::vector<int> &vect)
{
    std::vector<int> local_vect = vect;

    bool carry_flag = false;
    for (int j = vect.size() - 1; j >= 0; j--)
    {
        if (vect[j] + 1 == 10)
        {
            local_vect[j] = 0;
            if (j == 0)
            {
                carry_flag = true;
                break;
            }
        }
        else
        {
            local_vect[j] = vect[j] + 1;
            break;
        }
    }

    if (carry_flag)
    {
        local_vect.insert(local_vect.begin(), 1);
    }

    return local_vect;
}

//
// ############################################################################
//

int hourglass_sum(std::vector<std::vector<int>> arr)
{
    // Enforces a 3x3 or larger matrix
    if (arr.size() < 3 || arr[0].size() < 3)
    {
        throw std::invalid_argument("Func hourglass_sum() requires a 3x3 matrix");
    }

    // Assumes one or more hourglass will result in a value greater than -255
    int result = -255;

    // Iterating through rows
    for (int j = 0; j < arr.size() - 2; j++)
    {
        for (int i = 0; i < arr[0].size() - 2; i++)
        {
            int sum = arr[j][i] + arr[j][i + 1] + arr[j][i + 2] + arr[j + 1][i + 1] + arr[j + 2][i] + arr[j + 2][i + 1]
                      + arr[j + 2][i + 2];
            if (sum > result)
            {
                result = sum;
            }
        }
    }
    return result;
}

//
// ############################################################################
//

std::vector<int> rot_left(std::vector<int> arr, int d)
{
    // Data validation for d
    if (d < 0)
    {
        throw std::invalid_argument("The number to rotate the array must be positive");
    }

    std::vector<int> rot_a(arr.size());
    for (int j = 0; j < rot_a.size(); j++)
    {
        int new_index = j - d;
        // Rolls over to the end of the array
        while (new_index < 0)
        {
            // Adding a negative is subtracting a postive
            new_index += arr.size();
        }
        rot_a[new_index] = arr[j];
    }
    return rot_a;
}

//
// ############################################################################
//

int minimum_swaps(std::vector<int> arr)
{
    // Data validation to ensure swaps can occur
    if (arr.size() < 2)
    {
        throw std::invalid_argument("Input array must contain at least 2 elemnts.");
    }

    // (value, index)
    std::pair<int, int> arr_pos[arr.size()];
    for (int j = 0; j < arr.size(); j++)
    {
        arr_pos[j].first  = arr[j];
        arr_pos[j].second = j;
    }
    std::sort(arr_pos, arr_pos + arr.size());

    std::vector<bool> vis(arr.size(), false);

    int num_swaps = 0;

    for (int i = 0; i < arr.size(); i++)
    {
        // already swapped and corrected or
        // already present at correct pos
        if (vis[i] || arr_pos[i].second == i)
            continue;

        // find out the number of node in
        // this cycle and add in ans
        int cycle_size = 0;
        int j          = i;
        while (!vis[j])
        {
            vis[j] = true;

            // move to next node
            j = arr_pos[j].second;
            cycle_size++;
        }

        // Update answer by adding current cycle.
        if (cycle_size > 0)
        {
            num_swaps += (cycle_size - 1);
        }
    }

    return num_swaps;
}

//
// ############################################################################
//

int64_t array_manipulation(int n, std::vector<std::vector<int>> queries)
{
    // Data Validation to ensure the proper format
    for (int j = 0; j < queries.size(); j++)
    {
        if (queries[j].size() != 3)
        {
            throw std::invalid_argument("All queries must contain 3 arguments");
        }
    }

    // Initialize all 0 array
    std::vector<int64_t> arr(n, 0);
    // Marks the steps up and down in the new array
    for (int64_t j = 0; j < queries.size(); j++)
    {
        arr[queries[j][0] - 1] += queries[j][2];
        if (queries[j][1] != arr.size())
        {
            arr[queries[j][1]] -= queries[j][2];
        }
    }

    int64_t counter     = 0;
    int64_t largest_num = 0;
    // Iterating through the array in order will find the largest sum
    // since the steps up and down are marked
    for (int64_t i = 0; i < arr.size(); i++)
    {
        counter += arr[i];
        if (counter > largest_num)
        {
            largest_num = counter;
        }
    }

    return largest_num;
}


//
// ############################################################################
//

int minimum_bribes(std::vector<int> arr)
{
    int min_swaps = 0;
    for (int j = arr.size() - 1; j >= 0; j--)
    {
        // Converts list to base 0 before checking if it's more than 2 ahead of original position
        if (((arr[j] - 1) - j) > 2)
        {
            throw std::invalid_argument("Too chaotic");
        }
        for (int i = std::max(0, arr[j] - 2); i < j; i++)
        {
            if (arr[i] > arr[j])
            {
                min_swaps++;
            }
        }
    }
    return min_swaps;
}

//
// ############################################################################
//

bool check_magazine(std::vector<std::string> magazine, std::vector<std::string> ransom)
{
    bool                                 note_in_mag_flag = true;
    std::unordered_map<std::string, int> words;
    for (auto &it : magazine)
    {
        words[it]++;
    }
    for (auto &it : ransom)
    {
        if (words[it] > 0)
        {
            words[it]--;
        }
        else
        {
            note_in_mag_flag = false;
        }
    }
    return note_in_mag_flag;
}

//
// ############################################################################
//

bool two_string_common_char(std::string s1, std::string s2)
{
    bool                          result = false;
    std::unordered_map<char, int> chars;
    for (auto &c1 : s1)
    {
        chars[c1]++;
    }
    for (auto &c2 : s2)
    {
        if (chars[c2] > 0)
        {
            chars[c2]--;
            result = true;
            break;
        }
    }
    return result;
}

//
// ############################################################################
//

std::vector<int> freq_query(std::vector<std::vector<int>> queries)
{
    std::vector<int>   frequency_queries;
    std::map<int, int> by_value;
    std::map<int, int> by_frequency;

    for (auto &q : queries)
    {
        if (q[0] == 1)
        {
            by_value[q[1]]++;
            by_frequency[by_value[q[1]]]++;
            if (by_value[q[1]] != 1)
            {
                by_frequency[by_value[q[1]] - 1]--;
            }
        }
        else if (q[0] == 2)
        {
            auto by_value_temp = by_value[q[1]];
            if (by_value_temp > 0)
            {
                by_frequency[by_value_temp]--;
                by_frequency[by_value_temp - 1]++;
                by_value[q[1]]--;
            }
        }
        else if (q[0] == 3)
        {
            int result = 0;
            if (by_frequency[q[1]] > 0)
            {
                result = 1;
            }
            frequency_queries.push_back(result);
        }
        else
        {
            throw std::invalid_argument("First value in pair must be 1, 2, or 3.");
        }
    }
    return frequency_queries;
}

//
// ############################################################################
//

std::vector<std::pair<int, int>> get_overlapping_intervals(std::vector<std::pair<int, int>> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i].first > arr[i].second)
        {
            throw std::invalid_argument("Intervals must be of the following format: (x,y) where y > x");
        }
    }

    std::sort(arr.begin(), arr.end());

    std::vector<std::pair<int, int>> output_arr;
    bool                             new_interval = false;

    output_arr.push_back(std::make_pair(arr[0].first, arr[0].second));
    for (int i = 1; i < arr.size(); i++)
    {
        // If intervals overlap
        if (arr[i].first < output_arr.back().second)
        {
            output_arr.back().second = arr[i].second;
        }
        else
        {
            new_interval = true;
        }

        if (new_interval)
        {
            output_arr.push_back(std::make_pair(arr[i].first, arr[i].second));
            new_interval = false;
        }
    }
    return output_arr;
}
} // namespace hacker_rank
