class Solution:
    def jump(self, nums: list[int]) -> int:
        current=0
        jump=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i == current:
                jump+=1
                current=farthest
        return jump
