"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int, visited=None) -> bool:
        if visited is None:
            visited = set()
        if(n == 1):
            return True
        if n in visited:
            return False
        visited.add(n)
        squareSum = sum([int(x) ** 2 for x in str(n)])
        return self.isHappy(squareSum, visited)
