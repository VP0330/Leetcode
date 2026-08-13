class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[0]*(len(triangle)+1)
        for r in triangle[::-1]:
            for i, n in enumerate(r):
                dp[i]=n+min(dp[i],dp[i+1])
        return dp[0]