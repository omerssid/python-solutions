"""
# 1779. Find Nearest Point That Has the Same X or Y Coordinate.

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

## Constraints:
1 <= points.length <= 104
points[i].length == 2
1 <= x, y, ai, bi <= 104
"""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhDis = 10000
        min_index = -1
        for i, p in enumerate(points):
            if (x == p[0]) or (y == p[1]):
                temp = abs(x - p[0]) + abs(y - p[1])
                if temp < manhDis:
                    manhDis = temp
                    min_index = i
        return min_index
