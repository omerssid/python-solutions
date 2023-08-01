"""
1232. Check If It Is a Straight Line
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coords_s = sorted(coordinates)
        x1, x2, y1, y2 = 0, 0, 0, 0
        slope = False
        for i in range(1, len(coords_s)):
            # m=(y2−y1)/(x2−x1) 
            dx = (coords_s[i][0]-coords_s[i-1][0])
            if dx == 0: # check for div by zero 
                m = math.inf
            else:
                dy = (coords_s[i][1]-coords_s[i-1][1]) 
                m = dy / dx
            if i == 1: # init slope
                slope = m
                continue
            if m != slope:
                return False
        return True 
