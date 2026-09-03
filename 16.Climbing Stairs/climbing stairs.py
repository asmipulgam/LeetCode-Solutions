class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2,s=1,1,0
        
        for i in range(n-1):
            s=s1+s2
            s1=s2
            s2=s
        return s2
