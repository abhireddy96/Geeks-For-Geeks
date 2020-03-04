"""
https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0
Given an input stream of N characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. If no non repeating element is found print -1.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def firstNonRepeatCharInStream(self, s: List[str]) -> List[str]:
        # Hash map to keep alphabet count
        alpha = dict()
        # Queue
        q = list()
        # Resultant array
        res = list()

        # Iterate over each alphabet in given list
        for c in s:
            # Add alphabet to queue
            q.append(c)
            # Increment alphabet count if already present in hash map, else make count 1
            if c in alpha:
                alpha[c] += 1
            else:
                alpha[c] = 1
            # Loop till queue is empty
            while q:
                # Remove repeating alphabets from queue
                if alpha[q[0]] > 1:
                    q.pop(0)
                # Add non-repeating alphabet to resultant array and stop current loop with break
                else:
                    res.append(q[0])
                    break
            # If queue is empty, add -1 to resultant array
            if not q:
                res.append('-1')
        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(*Solution().firstNonRepeatCharInStream(input().split()))
