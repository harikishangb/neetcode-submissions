class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnNums = []
        for n in range(len(nums)):
            multipliedValue = 1
            for i in range(len(nums)):
                if(n != i):
                    multipliedValue = multipliedValue * nums[i]
            
            returnNums.append(multipliedValue)
        
        return returnNums