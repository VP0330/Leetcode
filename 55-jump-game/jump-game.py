class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=0
        current=0
        farthest=0
        for i in range(len(nums)):
            farthest=max(farthest,i+nums[i])
            if i==current:
                jump+=1
                current=farthest
        return current>=len(nums)-1