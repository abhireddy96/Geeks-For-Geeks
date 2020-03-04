"""
https://practice.geeksforgeeks.org/problems/rightmost-different-bit/0
Given two numbers M and N. The task is to find the position of rightmost different bit in binary representation of numbers.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def rightDiffBit(self, nums: List[int]) -> int:
        # Convert to binary using bin()
        num1 = bin(nums[0])[2:]
        num2 = bin(nums[1])[2:]

        # Make two binary string equal in length by prefixing with '0's for min length binary string
        if len(num1) < len(num2):
            num1 = '0'*(len(num2)-len(num1))+num1

        elif len(num2) < len(num1):
            num2 = '0' * (len(num1) - len(num2)) + num2

        # Iterate in reverse order
        for i in range(len(num1)-1, -1, -1):
            # Check if corresponding value of bit is different a ith position
            # If not return position
            if num1[i] != num2[i]:
                return len(num1)-i
        return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().rightDiffBit(list(map(int, input().split()))))
