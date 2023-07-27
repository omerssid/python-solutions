class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # if low if even, make it odd
        if (low % 2)==0:
            low +=1
        return 0 if low > high else int((high-low)/2)+1
