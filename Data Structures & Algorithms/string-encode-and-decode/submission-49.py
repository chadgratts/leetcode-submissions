class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(s)}${s}' for s in strs])
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            l = int(s[i:j])
            start = j + 1
            end = j + l + 1
            res.append(s[start:end])

            i = end
        return res