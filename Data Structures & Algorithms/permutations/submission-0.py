class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutacje = self.permute(nums[1:])

        res = []
        for p in permutacje:
            for i in range(len(p) + 1):
                cop = p.copy()
                res.append(cop.insert(i,nums[0]))
            
        return res