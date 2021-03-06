"""
https://practice.geeksforgeeks.org/problems/maximum-number-of-zeroes/0
Given an array of N values. Print the number which has maximum number of zeroes. If there are no zeroes then print -1.
Note: If there are multiple numbers with same (max) number of zeroes then print the Maximum number among them. """
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def count_zeros(self, nums: List[int]) -> int:
        max_num = -1
        max_zeroes = 1

        # Iterate over list of integers
        for i in nums:
            # Count number of zeros
            # check if it's greater than max zeroes got so far
            if int(str(i).count('0')) > max_zeroes:
                max_zeroes = int(str(i).count('0'))
                max_num = int(i)
            # check if it's equal to  max zeroes got so far
            # If so, check if this integer is greater than previous best
            elif int(str(i).count('0')) == max_zeroes:
                if int(i) > max_num:
                    max_num = int(i)
        return max_num


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        a = [int(i) for i in input().split()]
        print(Solution().count_zeros(a))
