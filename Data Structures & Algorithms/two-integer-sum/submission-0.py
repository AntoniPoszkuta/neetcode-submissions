class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vals = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in vals:
                return [vals[diff],index]
            if num not in vals:
                vals[num] = index