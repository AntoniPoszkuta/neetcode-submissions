from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter(s1)
        checking = Counter(s2[:len(s1)])
        if window == checking:
            return True

        for i in range(len(s1),len(s2)):
            
            checking[s2[i - len(s1)]] -= 1

            checking[s2[i]] += 1

            if checking[s2[i - len(s1)]] == 0:
                del checking[s2[i - len(s1)]]

            if window == checking:
                return True
        
        return False