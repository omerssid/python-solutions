"""
1588. Sum of All Odd Length Subarrays
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if not arr:
            return 0

        oddSum = 0
        arrLen = len(arr)+1

        for x in range(1, arrLen, 2):
            for i in range(len(arr)-x+1):
                oddSum += sum(arr[i:x+i])
        return oddSum
