class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        tab = []
    
        def dfs(i,suma,tab):
            
            if suma == target:
                res.append(tab.copy())
                return
            if suma > target or i >= len(candidates):
                return
            
            tab.append(candidates[i])
            suma += candidates[i]
            dfs(i+1, suma, tab)
        
            tab.pop()
            suma -= candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
                
            dfs(i+1, suma ,tab)


        dfs(0,0,[])
        return res