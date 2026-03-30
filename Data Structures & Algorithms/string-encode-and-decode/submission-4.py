class Solution:

    def encode(self, strs: List[str]) -> str:
        # create empty string variable
        # iterate through the strings
        # encode: len and "@" f"{len(str)@{str}}"
        # return a string
        result = ""
        for s in strs:
            result += f"{len(s)}@{s}"
        
        return result

    def decode(self, s: str) -> List[str]:
        # iterate through the string
        # when you have a number followed by an "@", slice the string
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            length = int(s[i:j])

            word = s[j + 1:j + 1 + length]
            res.append(word)

            i = j + 1 + length

        return res
