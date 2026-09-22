class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        endings = {
            "}": "{",
            "]" : "[",
            ")" : "("
        }

        for char in s:
            if char in endings:
                if not stack or stack.pop() != endings[char]:
                    return False

            else:
                stack.append(char)
                
        return not stack