"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            counter += n % 2
            n = n >> 1
        return counter
