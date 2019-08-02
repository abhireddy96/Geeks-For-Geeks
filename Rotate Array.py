"""
https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
Input:
The first line of the input contains T denoting the number of testcases. First line of eacg test case contains two space separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent line will be the N space separated array elements.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def rotate(self, nums: List[int], r: int) -> List[int]:
        return nums[r:]+nums[:r]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, d = input().split()
        print(*Solution().rotate(list(map(int, input().split())), int(d)))
