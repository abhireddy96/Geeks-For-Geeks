"""
https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0
Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have any adjacent duplicates.
"""
__author__ = 'abhireddy96'
import string


class Solution:
    def removeDuplicates(self, s: string) -> string:
        res = []
        i = 0
        # Iterate over each character in string
        while i < len(s):
            # If current character is last character of result string
            if res and res[-1] == s[i]:
                # Loop till next different character
                j = i+1
                while j < len(s):
                    if s[i] == s[j]:
                        j += 1
                    else:
                        break
                # Remove last character from resultant string
                # Assign index of different character
                i = j
                res.pop()

            # If not, append character to resultant string
            else:
                res.append(s[i])
                i += 1

        return "".join(res)


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().removeDuplicates(input()))
