class Solution:
    # prefix and pointers
    # get the same list after turning list into str
    # meaning i need to get substrings from a str
    # using the len of strings and delimiter, i can slice the substr
    # turn each string into string of format len + delimiter + str
    # use two pointers, iterate until delimiter
    # slice from first pointer to second, that the length
    # index delimiter + 1 is where the string begins, slice using length
    # move pointer to the next substring chunk. if delimiter is in substring, it doesnt matter
    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(s)}#{s}' for s in strs])

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length

            strings.append(s[start:end])
            i = end
        return strings