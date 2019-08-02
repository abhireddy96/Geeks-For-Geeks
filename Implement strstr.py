"""https://practice.geeksforgeeks.org/problems/implement-strstr/1 Your task is to implement the function strstr. The
function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The
function returns and integer denoting the first occurrence of the string x in s """
__author__ = 'abhireddy96'
import string


class Solution:
    def strStr(self, haystack: string, needle: string) -> int:
        # if needle string is empty
        if not needle:
            return 0
        # if needle is present in haystack , return matching index
        if needle in haystack:
            return haystack.index(needle)
        # needle is not present in haystack
        return -1


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = input().split()
        print(Solution().strStr(a, b))

