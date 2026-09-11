class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    n[i]=max(n[i],1+n[j])
        return max(n)
