"""
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
NOTE: Required Time Complexity O(n2).
"""
__author__ = 'abhireddy96'


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Is string is empty
        if not s:
            return s
        # Contains single character
        if len(s) == 1:
            return s

        # Let first character be resultant palindrome
        res = s[0]

        # Iterate over string characters
        for i in range(0, len(s)):

            # Check for Palindrome odd length
            cur = self.palindrome_from_center(s, i, i)
            if len(cur) > len(res):
                res = cur

            # Check for Palindrome even length
            cur = self.palindrome_from_center(s, i, i + 1)
            if len(cur) > len(res):
                res = cur

        return res

    # find palindrome from center
    def palindrome_from_center(self, s, begin, end):

        # Traverse Outwards from given index
        # Check that string index is not out of range
        # left and right characters should match in order to be palindromic string
        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            # Move towards left of string
            begin -= 1
            # Move towards right of string
            end += 1
        return s[begin + 1: end]


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().longestPalindrome(input()))
