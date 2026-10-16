class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mini = 999999
        while l <= r:
            
            mid = (r + l) // 2

            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

            mini = nums[mid] if nums[mid] < mini else mini
        
        return mini