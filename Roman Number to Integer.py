"""
https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0
Given an string in roman no format (s)  your task is to convert it to integer .
"""
__author__ = 'abhireddy96'


class Solution:
    def romanToInt(self, s: str) -> int:
        # Hash map of Values to be added
        adds = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # Hash map of Values to be subtracted (For Special case Roman letters)
        subs = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
        res = 0

        # Special case Roman letter = right roman letter - left roman letter
        # Eg: IV = V-I i.e 4=5-1

        # Iterate over each roman letter
        for c in s:
            # Add corresponding value of roman letter to result
            res += adds[c]

        # Iterate over each roman letter again
        for c in subs:
            # Subtract corresponding value of Special case roman letter from result
            if c in s:
                res -= subs[c]
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().romanToInt(input()))
