from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()

        openings = set(['(','[','{'])

        endings = {
            "}": "{",
            "]" : "[",
            ")" : "("
        }

        for char in s:
            if char in openings:
                stack.put(char)
            else:
                if stack.empty() or stack.get() != endings[char]:
                    return False

        return stack.empty()