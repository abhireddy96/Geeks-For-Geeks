"""
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def sort012(self, nums: List[int]) -> List[int]:
        return list(sorted(nums))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input().split()
        print(*Solution().sort012(list(map(int, input().split()))))
