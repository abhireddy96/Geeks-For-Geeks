"""
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def reverse(self, s: string) -> string:
        return '.'.join(s.split('.')[::-1])


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().reverse(input()))
