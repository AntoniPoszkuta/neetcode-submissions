class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            mid = (r + l) // 2

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if l >= len(nums):
            l = len(nums) - 1
        elif l < 0:
            l = 0
        return nums[l]