"""
https://practice.geeksforgeeks.org/problems/inversion-of-array/0/
Given an array of positive integers. The task is to find inversion count of array.
Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def inverse(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
        return cnt


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().inverse(list(map(int, input().split()))))
