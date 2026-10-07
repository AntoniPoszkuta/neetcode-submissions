class Solution:

    def getArea(self, ind1, ind2, h1, h2):
        return (ind2 - ind1) * min(h1, h2)
    
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        if len(heights) <= 1:
            return 0

        l = 0
        r = len(heights) - 1

        while l < r:
            area = self.getArea(l,r,heights[l],heights[r])
            if area > maxi:
                maxi = area
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxi

