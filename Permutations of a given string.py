"""
https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
Given a string S. The task is to print all permutations of a given string
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def permute(self, s: string) -> string:
        res = list()
        self.compute('', s, res)
        return res

    # Recursive function
    def compute(self, p: string, s: string, res):

        # Base case : If string is empty
        if not s:
            # one of permutation is prefix + remaining string
            res.append(p+s)
            return

        # Iterate over each character
        for i in range(len(s)):
            # Prefix = current prefix + current character
            # String = Characters right to current character
            self.compute(p + s[i], s[0: i] + s[i + 1: len(s)], res)


if __name__ == "__main__":
    for _ in range(int(input())):
        print(*Solution().permute(input()))
