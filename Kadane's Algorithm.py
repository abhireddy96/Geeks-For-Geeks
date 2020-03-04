"""
https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        beg = 1
        end = 1
        res = nums[0]
        while beg < len(nums) and end <= len(nums):
            if res == target:
                return [beg + 1, end]
            else:
                if res > target:
                    res -= nums[beg]
                    beg += 1
                else:
                    if end == len(nums):
                        return [-1]
                    res += nums[end]
                    end += 1
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(Solution().max_sub_array(a))
