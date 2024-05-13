"""
problem: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
"""
from typing import List


class Solution:

    def solve_recursively(self, energy: List[int], k, idx, n, memo):
        if idx >= n:
            return 0
        if memo[idx] != float("-inf"):
            return memo[idx]
        memo[idx] = energy[idx] + self.solve_recursively(energy, k, idx + k, n, memo)
        return memo[idx]
    def maximum_energy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        n = len(energy)
        memo = []
        for i in range(n):
            memo.append(float("-inf"))

        for i in range(n):
            ans = max(ans, self.solve_recursively(energy, k, i, n, memo))

        return ans


# Test cases
def test_solution():
    solution = Solution()

    # Test case 1: Basic scenario
    assert solution.maximum_energy([5, 2, -10, -5, 1], 3) == 3

    # Test case 2: All elements have the same energy value
    assert solution.maximum_energy([-2, -3, -1], 2) == -1

    print("All test cases pass")


test_solution()
