class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for word in strs:

            sorted_anagram = "".join(sorted(word))

            if sorted_anagram not in dic:
                dic[sorted_anagram] = [word]
            else:
                dic[sorted_anagram].append(word)
        
        return list(dic.values())