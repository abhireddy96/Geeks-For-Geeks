"""
https://practice.geeksforgeeks.org/problems/next-larger-element/0
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def nextLarger(self, nums: List[int]) -> List[int]:
        res = list()
        stack = list()
        # Iterate over list of integers in reverse order
        for i in range(len(nums)-1, -1, -1):
            # Loop till stack is not empty and current element is greater than stack top element
            # Remove the top element if condition is true, finally remaining top element is greater than current element
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            # If stack is not empty, Add top element of stack to resultant array
            res.insert(0, stack[-1] if stack else -1)
            # Add current element to stack
            stack.append(nums[i])
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(*Solution().nextLarger(list(map(int, input().split()))))
