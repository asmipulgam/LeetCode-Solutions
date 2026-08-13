class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist={}
        for i, num in enumerate(nums):
            s=target-nums[i]
            if s in exist:
                return [exist[s],i]
            exist[num]=i
        return []
