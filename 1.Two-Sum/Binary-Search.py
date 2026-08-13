class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[(num,i) for i, num in enumerate(nums)]
        arr.sort()
        for i in range(len(arr)):
            curr=arr[i][0]
            s=target-curr
            l,r=i+1, len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid][0]==s:
                    return [arr[i][1],arr[mid][1]]
                elif s>arr[mid][0]:
                    l=mid+1
                else:
                    r=mid-1
        return []
