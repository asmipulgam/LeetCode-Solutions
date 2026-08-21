class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1, len(nums)-1
            while l<r:
                if (nums[l]+nums[r]+nums[i])==0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

                elif nums[l]+nums[r]+nums[i]<0:
                    l+=1
                else:
                    r-=1
        return res
