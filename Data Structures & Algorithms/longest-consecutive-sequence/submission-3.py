class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sortNums = sorted(nums)
        current = 1
        best = 1
        
        for i in range(1, len(sortNums)):
            if sortNums[i] == sortNums[i - 1]:
                continue
            if sortNums[i] == sortNums[i - 1] + 1:
                current += 1
            else:
                best = max(best, current)
                current = 1
        
        best = max(best, current)
        return best