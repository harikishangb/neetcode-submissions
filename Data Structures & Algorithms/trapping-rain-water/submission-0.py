class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        runningMax = 0
        waterLevel = 0
        for h in range(len(height)):
             leftMax.append(runningMax)
             runningMax = max(runningMax, height[h])
        runningMax = 0
        for i in range(len(height) - 1, -1, -1):
             rightMax.append(runningMax)
             runningMax = max(runningMax, height[i])
        rightMax.reverse()
        for r in range(len(height)):
             if min(leftMax[r], rightMax[r]) - height[r] > 0:
                  runningLevel = min(leftMax[r], rightMax[r]) - height[r]
             else:
                  runningLevel = 0
             waterLevel = waterLevel + runningLevel
        return waterLevel