"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
"""
__author__ = 'abhireddy96'


class Solution:
    def isValid(self, s: str) -> bool:
        # Hash map of closing and opening parenthesis
        d = {')': '(', ']': '[', '}': '{'}
        ls = []
        # Iterate over string
        for i in s:
            # Check if it is closing parenthesis
            if i in d:
                # If so, pop top element from stack
                sym = ls.pop() if ls else ''
                # Compare if parenthesis of same type
                # If not immediately return False
                if d[i] != sym:
                    return 'not balanced'
            # Check if it is opening parenthesis
            # Add it to stack
            else:
                ls.append(i)
        return 'balanced' if ls == [] else 'not balanced'


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().isValid(input()))
