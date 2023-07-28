"""
# 1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(0, len(arr)-1):
            if i == 0:
                diff = arr[i] - arr[i+1]
                continue
            if diff !=  arr[i] - arr[i+1]:
                return False
        return True
