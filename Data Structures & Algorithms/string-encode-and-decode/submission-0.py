class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for words in strs:
            result = result + str(len(words)) + "#" + words
        return result
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j+1+length
        return res