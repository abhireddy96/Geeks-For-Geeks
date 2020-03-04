"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def kSmallest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[k - 1]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().kSmallest(list(map(int, input().split())),int(input())))
