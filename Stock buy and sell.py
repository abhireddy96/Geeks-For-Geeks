"""
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def stocks(self, nums: List[int]) -> List:
        beg = 0
        end = 1
        res = list()

        # Iterate with two pointers over list of integers
        while beg < len(nums) and end < len(nums):
            # Check if current day stock price is greater than previous day
            if nums[end] > nums[end-1]:
                # If so proceed to next day
                end += 1
                # check if it is last stock in list, means no loss from beg day -> Add to result
                if end == len(nums):
                    res.append('(' + str(beg) + ' ' + str(end - 1) + ')')
            # If not, consider current day as beg
            else:
                # Check that there should be at least one day difference
                # Add to result
                if end - beg != 1:
                    res.append('('+str(beg)+' '+str(end-1)+')')
                beg = end
                end += 1
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        result = Solution().stocks(list(map(int, input().split())))
        if not result:
            print("No Profit")
        else:
            print(*result)
