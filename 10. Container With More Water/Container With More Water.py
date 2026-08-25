class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r =0, len(height)-1
        area,maxi=0,0
        while l<=r:
            area=(r-l)*min(height[l],height[r])
            maxi=max(area,maxi)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi
