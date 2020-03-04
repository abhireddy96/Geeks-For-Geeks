"""
https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
"""
__author__ = 'abhireddy96'
from typing import List
import string


class Solution:
    def triplet(self, nums: List[int]) -> string:
        nums = [i*i for i in sorted(nums)]
        print(nums)
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if nums[i] + nums[j] in nums:
                    return 'Yes'
        return 'No'


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().triplet(list(map(int, input().split()))))
