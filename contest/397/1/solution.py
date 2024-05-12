"""
problem: https://leetcode.com/problems/permutation-difference-between-two-strings/
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> str:
        ans = 0
        letter_index_map = {letter: index for index, letter in enumerate(t)}
        for index, letter in enumerate(s):
            ans += abs(letter_index_map[letter] - index)
        return ans


# Test cases
def test_solution():
    solution = Solution()
    assert solution.findPermutationDifference("abc", "bac") == 2
    assert solution.findPermutationDifference("abcde", "edbac") == 12
    print("All test cases pass")


test_solution()
