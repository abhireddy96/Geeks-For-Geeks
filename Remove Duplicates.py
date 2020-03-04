"""
https://practice.geeksforgeeks.org/problems/remove-duplicates/0
Given a string, the task is to remove duplicates from it. Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.
Note: that original order of characters must be kept same.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def removeDuplicates(self, s: string) -> string:
        res = ''
        # Iterate over each character in string
        for c in s:
            # Check if character is already in resultant string
            # If not append it to resultant string
            if c not in res:
                res += c
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().removeDuplicates(input()))
