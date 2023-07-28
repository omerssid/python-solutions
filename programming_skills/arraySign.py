"""
# 1822. Sign of the Product of an Array

We are given an integer array nums. Our task is to return the sign of the product of all values in the array nums.
"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negativeCounter = 0
        for n in nums:
            if n==0:
                return 0
            elif n < 0:
                negativeCounter += 1
        return 1 if (negativeCounter % 2 == 0) else -1
