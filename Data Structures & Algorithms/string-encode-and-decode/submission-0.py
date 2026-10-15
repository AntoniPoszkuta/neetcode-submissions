class Solution:

    def encode(self, strs: List[str]) -> str:
        
        message = ""

        if len(strs) == 0:
            return ""

        for word in strs:
            message += str(len(word)) + "#" + word

        return message


    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
        
        message = []

        index = 0

        while index < len(s):
            
            new_word = ""

            new_len = ""

            while s[index] != "#":
                new_len += s[index]
                index += 1

            index += 1

            for _ in range(int(new_len)):
                new_word += s[index]
                index += 1

            message.append(new_word)

        return message
