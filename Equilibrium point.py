"""
https://practice.geeksforgeeks.org/problems/equilibrium-point/0
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def equilibriumPoint(self, nums: List[int]) -> int:
        # Calculate Total Sum
        total_sum = sum(nums)
        left_sum = 0
        # Iterate from starting index
        for i, v in enumerate(nums):
            # Subtract value from total sum
            total_sum -= v
            if left_sum == total_sum:
                return i+1
            # Add value to left sum
            left_sum += v
        # equilibrium point not found
        return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().equilibriumPoint(list(map(int, input().split()))))
