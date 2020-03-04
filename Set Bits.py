"""
https://practice.geeksforgeeks.org/problems/set-bits/0/
Given a positive integer N, print count of set bits in it. For example, if the given number is 6(binary: 110), output should be 2 as there are two set bits in it.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def setBits(self, num: int) -> string:
        return bin(num).count('1')


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().setBits(int(input())))
