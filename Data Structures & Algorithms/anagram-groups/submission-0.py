class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        group_map = {}
        for word in strs:
            secret_code = "".join(sorted(word)) 
            if secret_code in group_map:
                group_map[secret_code].append(word)
            else:
                group_map[secret_code] = [word]
        return list(group_map.values())
