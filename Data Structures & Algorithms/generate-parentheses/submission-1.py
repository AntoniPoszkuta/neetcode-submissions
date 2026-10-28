class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n, to_put, word):
            if n <= 0:
                while to_put > 0:
                    word += ")"
                    to_put -= 1
                res.append(word)
                return
            
            word += "("

            dfs(n-1, to_put+1,word)

            word += ")"
            
            dfs(n-1, to_put, word)

        dfs(n,0,"")
        return res