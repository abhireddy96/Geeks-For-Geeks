"""
https://practice.geeksforgeeks.org/problems/find-first-set-bit/0
Given an integer an N. The task is to print the position of first set bit found from right side in the binary representation of the number.
"""
__author__ = 'abhireddy96'


class Solution:
    def firstSetBit(self, nums: str) -> int:
        res = bin(nums)[2:]
        for i in range(len(res)-1, -1, -1):
            if res[i] == '1':
                return len(res)-i
        return 0


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().firstSetBit(int(input())))
