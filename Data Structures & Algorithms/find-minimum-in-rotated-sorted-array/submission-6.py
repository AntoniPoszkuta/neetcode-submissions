class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                # Minimum jest w prawej części (za mid)
                l = mid + 1
            else:
                # Minimum jest w lewej części lub to sam mid
                r = mid
                
        return nums[l]