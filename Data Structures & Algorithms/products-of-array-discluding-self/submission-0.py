class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        output = []
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        
        if zeros == 0:
            return [int(product/num) for num in nums]
        elif zeros == 1:
            for num in nums:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            return output
        else:
            return [0 for _ in range(len(nums))]