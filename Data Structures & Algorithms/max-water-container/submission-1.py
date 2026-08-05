class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftWall = 0
        rightWall = len(heights) - 1
        maximumCapacity = 0
        while leftWall < rightWall:
                width = rightWall - leftWall
                if heights[leftWall] > heights[rightWall]:
                     currentCapacity = width * heights[rightWall]
                     rightWall -=1
                else:
                     currentCapacity = width * heights[leftWall]
                     leftWall +=1
                maximumCapacity = max(maximumCapacity, currentCapacity)

        return maximumCapacity