"""
https://practice.geeksforgeeks.org/problems/last-index-of-1/0
Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def lastIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if nums[i] == 1:
                return i
        return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().lastIndex(list(map(int, input()))))
