class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for word in strs:
            if "".join(sorted(word)) not in dic:
                dic["".join(sorted(word))] = [word]
            else:
                dic["".join(sorted(word))].append(word)
        
        new = []

        for val in dic.values():
            new.append(val)

        return new