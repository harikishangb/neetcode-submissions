class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        returnNums = [1] * n

        prefix = 1
        for i in range(n):
            returnNums[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            returnNums[i] *= suffix
            suffix *= nums[i]
    
        return returnNums