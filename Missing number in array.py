"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)+1
        # Find sum of n integers using S(n) = n(n+1)/2 formula
        total_sum = n * (n+1) // 2
        # Find sum of array elements
        obtained_sum = sum(nums)
        # Missing number is (sum of n integers) - (sum of array elements)
        return total_sum - obtained_sum


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().missingNumber(list(map(int, input().split()))))
