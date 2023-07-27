"""
# 1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(x) for x in str(n) ]
        productof = 1
        sumof = 0
        for i in res:
            productof *= i
            sumof += i
        return productof - sumof
