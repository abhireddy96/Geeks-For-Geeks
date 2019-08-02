"""
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def isAnagram(self, s: string, t: string) -> string:
        # Make everything lowercase
        # Trim spaces
        # Sort characters
        s = sorted(s.replace(' ', '').lower())
        t = sorted(t.replace(' ', '').lower())
        return 'YES' if s == t else 'NO'


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = input().split()
        print(Solution().isAnagram(a, b))
