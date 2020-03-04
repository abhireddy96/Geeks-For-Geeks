"""
https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0
Given two strings a and b. The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def rotate(self, s1: string, s2: string) -> string:
        return 1 if s1 == s2[2:] + s2[0:2] or s1 == s2[-2:] + s2[:-2] else 0


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().rotate(input(), input()))
