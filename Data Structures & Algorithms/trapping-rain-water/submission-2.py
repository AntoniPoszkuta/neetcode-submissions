class Solution:

    def trap(self, height: List[int]) -> int:
        result = 0

        l = 0
        r = len(height) - 1
        l_max, r_max = height[l] ,height[r]
        while l < r:

            if l_max > r_max:
                r -= 1
                r_max = max(r_max,height[r])
                result += r_max - height[r]
            else:
                l += 1
                l_max = max(l_max,height[l])
                result += l_max - height[l]
                
 
        return result