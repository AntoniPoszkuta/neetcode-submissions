class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        if s == "":
            return 0
        
        chars = set()
        
        while r < len(s):
            chars.add(s[r])

            if r - l + 1 > longest:
                longest = r - l + 1
            
            r += 1

            while len(chars) > 0 and r < len(s) and s[r] in chars:
                chars.remove(s[l])
                l += 1
             

        return longest
            