"""
https://practice.geeksforgeeks.org/problems/count-the-triplets/0
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element. """
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def count_triplets(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        nums = sorted(nums)
        max_num = max(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                s = nums[i] + nums[j]
                if s > max_num:
                    break
                if s in nums[j+1:]:
                    cnt += 1

        return cnt if cnt > 0 else -1


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        a = [int(i) for i in input().split()]
        print(Solution().count_triplets(a))
