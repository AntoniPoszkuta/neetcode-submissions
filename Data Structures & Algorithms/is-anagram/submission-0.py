class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        a, b = [], []

        for n in range(len(s)):
            a.append(s[n])
            b.append(t[n])
        
        a = sorted(a)
        b = sorted(b)

        for n in range(len(s)):
            if a[n] != b[n]:
                return False
        
        return True