class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        maxi = 0

        for num in nums:

            if num - 1  not in nums:
                
                counter = 1
                tmp = num

                while tmp + 1 in nums:
                    tmp += 1
                    counter += 1
            
                if counter > maxi:
                    maxi = counter

        return maxi
                

