class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = slow+1 if slow+1 < len(nums) else 0
            fast = fast+2 if fast+2 < len(nums) else 0
            if nums[slow] == nums[fast] and slow != fast:
                return nums[slow]
        return -1

        # ememememe imimimi eme euee