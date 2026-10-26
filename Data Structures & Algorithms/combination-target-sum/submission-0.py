class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums2 = []
        for num in nums:
            if num <= target:
                nums2.append(num)
        nums = nums2

        res = []

        def dfs(i, suma, tab):
            
            if suma == target:
                res.append(tab.copy())
                return
            elif suma > target or i >= len(nums):
                return
            
            tab.append(nums[i])
            suma += nums[i]
            dfs(i,suma,tab)
            tab.pop()
            suma -= nums[i]
            dfs(i+1,suma,tab)

        dfs(0,0,[])

        return res