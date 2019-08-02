"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def sub_array(self, nums: List[int], target: int) -> List[int]:

        beg = 0
        end = 0
        res = 0

        # Iterate over list with two pointers
        while beg < len(nums) and end <= len(nums):
            # If sum of sub array equals target
            if res == target:
                return [beg+1, end]
            else:
                # Check sum of of current sub array greater than target
                if res > target:
                    # Increment beg index
                    res -= nums[beg]
                    beg += 1
                # Check sum of of current sub array less or equal than target
                else:
                    # Check if reached last index, then return -1
                    if end == len(nums):
                        return [-1]
                    # Increment end index
                    res += nums[end]
                    end += 1
        # not found
        return [-1]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, s = input().split()
        a = [int(i) for i in input().split()]
        print(*Solution().sub_array(a, int(s)))
