class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        permute=self.permute(nums[1:])
        res=[]
        for i in permute:
            for j in range(len(i)+1):
                copy=i.copy()
                copy.insert(j,nums[0])
                res.append(copy)
        return res
