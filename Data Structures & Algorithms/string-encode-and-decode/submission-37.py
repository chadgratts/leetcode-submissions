class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i + 1

            # "5#Hello5#World"
            while j < len(s):
                if s[j] == "#":
                    length = int(s[i:j])
                    res.append(s[j + 1: j + 1 + length])
                    i = j + 1 + length
                    break
                j += 1
        
        return res
            