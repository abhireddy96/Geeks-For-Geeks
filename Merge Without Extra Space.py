"""
https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0
Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).
Note: Expected time complexity is O((n+m) log(n+m)). DO NOT use extra space.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def merge(self, a : List[int], b: List[int]) -> List[int]:
        i = 0
        j = 0
        res = list()

        # Iterate over both lists using separate pointers until size of smaller list
        while i < len(a) and j < len(b):
            # Check if element of first list is smaller than that of second list
            # Add it to resultant list if smaller, also increment index of first list
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            # Add it to resultant list if smaller, also increment index of second list
            else:
                res.append(b[j])
                j += 1

        # Append remaining elements of first list(Bcoz size of second list is less than first )
        if i < len(a):
            res += a[i:]

        # Append remaining elements of second list(Bcoz size of first list is less than second )
        if j < len(b):
            res += b[j:]

        return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n1, n2 = input().split()
        print(*Solution().merge(list(map(int, input().split())), list(map(int, input().split()))))
