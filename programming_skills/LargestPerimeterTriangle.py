"""
# 976. Largest Perimeter Triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Solution:
1. Sort the list in reverse to get the top 3 lengths
2. loop through the list
   2.1 check if top 3 can form a triangle
   2.2 if true return the sum of all lengths
   2.3 if false drop the max length and repeat 2.1
3. If if no solution exists then the function returns 0.
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
