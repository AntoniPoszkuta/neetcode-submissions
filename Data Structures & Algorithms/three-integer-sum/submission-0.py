class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = []
        nums.sort()
        if len(nums) < 3:
            return []

        l = 0
        r = len(nums) - 1

        for p in range(len(nums) - 1):
            if p > 0 and nums[p] == nums[p - 1]:
                continue
            
            l = p + 1
            r = len(nums) - 1
            
            while l < r:
                suma = nums[p] + nums[l] + nums[r]

                if suma == 0:
                    pairs.append([nums[p],nums[l],nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif suma < 0:
                    l += 1
                else:
                    r -= 1

                

        return pairs