"""
# 1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter = 0
        if sorted(s1) != sorted(s2):
            return False
        for i,s in enumerate(s1):
            if (s != s2[i]):
                counter += 1
        return False if counter > 2 else True
