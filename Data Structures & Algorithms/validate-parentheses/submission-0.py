class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack or stack[-1] != close_to_open[char]:
                    return False
                stack.pop()
                
        return len(stack) == 0