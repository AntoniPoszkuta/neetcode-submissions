class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        endings = {
            "}": "{",
            "]" : "[",
            ")" : "("
        }

        for char in s:
            if char in endings.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != endings[char]:
                    return False

        return not stack