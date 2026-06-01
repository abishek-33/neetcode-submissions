class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False    
        char_counts = {}    

        for char in s:  
            char_counts[char] = char_counts.get(char, 0)+1
        for char in t:  
            char_counts[char] = char_counts.get(char, 0)-1
        for count in char_counts.values():
            if count != 0:
                return False

        return True    



 