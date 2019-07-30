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
        while beg < len(nums) and end <= len(nums):
            if res == target:
                return [beg+1, end]
            else:
                if res > target:
                    res -= nums[beg]
                    beg += 1
                else:
                    if end == len(nums):
                        return [-1]
                    res += nums[end]
                    end += 1
        return [-1]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, s = input().split()
        a = [int(i) for i in input().split()]
        print(*Solution().sub_array(a, int(s)))
