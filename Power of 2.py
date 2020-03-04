"""
https://practice.geeksforgeeks.org/problems/power-of-2/0
Given a positive integer N. The task is to check if N is a power of 2. That is N is 2x for some x.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def powerOf2(self, num:int) -> string:
        return 'YES' if num == 0 or bin(num).count('1') == 1 else 'NO'


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().powerOf2(int(input())))
