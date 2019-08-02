"""
https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def findLeaders(self, nums: List[int]) -> List[int]:
        res = list()
        # Consider last element as Pivot, add it to resultant array as last or rightmost element is always Leader
        pivot = nums[-1]
        res.append(pivot)

        # Iterate from penultimate to starting index
        for i in range(len(nums)-2, -1, -1):
            # Element should be greater that pivot, in order to be Leader
            if nums[i] >= pivot:
                pivot = nums[i]
                res.append(pivot)
        # Reverse resultant array
        return list(reversed(res))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().findLeaders(list(map(int, input().split()))))
