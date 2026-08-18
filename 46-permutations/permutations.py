class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        res=[]
        permute=self.permute(nums[1:])
        for i in permute:
            for j in range(len(i)+1):
                i_copy=i.copy()
                i_copy.insert(j,nums[0])
                res.append(i_copy)
        return res