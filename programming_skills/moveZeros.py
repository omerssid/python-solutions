"""
283. Move Zeroes
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # zeros count
        snowBallSize = 0
        for n in range(len(nums)):
            if nums[n] == 0:
                snowBallSize += 1
            else:
                nums[n], nums[n-snowBallSize] =  0, nums[n]
