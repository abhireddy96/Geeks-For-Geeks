"""
https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0
Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
"""
__author__ = 'abhireddy96'


class Solution:
    def longestDistinctSubstring(self, s: str) -> int:
        ls = []
        # Max number of distinct characters
        m = 0
        # Iterate over string
        for x in s:
            # check if character already present in distinct character list,
            # if so remove all the elements to it's left
            if x in ls:
                ls = ls[ls.index(x) + 1:]
            # Append character to right
            ls.append(x)
            # Check if length of distinct character list is greater than previous best
            m = max(m, len(ls))

        return m


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().longestDistinctSubstring(input()))
