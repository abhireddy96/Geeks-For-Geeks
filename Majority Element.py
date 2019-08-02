"""
https://practice.geeksforgeeks.org/problems/majority-element/0
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize empty hash map or dictionary, integer as keys and count or occurrence as value
        res = dict()
        max_count = 0
        max_num = -1

        # Iterate over list or array
        for i in nums:
            # If integer already present in hash map
            if i in res:
                # Increment count
                res[i] += 1
                # If count of current integer is greater maximum count
                if res[i] > max_count:
                    # Consider current integer as integer with most occurrences
                    max_count = res[i]
                    max_num = i
            # If integer not present in hash map, add it to hash map and it's count as 1
            else:
                res[i] = 1

        return max_num if max_count > len(nums) // 2 else -1


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print(Solution().majorityElement(list(map(int, input().split()))))
