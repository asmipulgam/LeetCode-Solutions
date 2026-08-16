class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        cursum=0
        for i in range(len(nums)):
            if cursum<0:
                cursum=0
            cursum+=nums[i]
            maxsub=max(maxsub,cursum)
        return maxsub
