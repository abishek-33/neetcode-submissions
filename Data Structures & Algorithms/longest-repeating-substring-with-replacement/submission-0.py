class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # Update notebook scoreboard
            if current_char not in count:
                count[current_char] = 0
            count[current_char] += 1
            
            # Calculate current window stats
            window_size = right - left + 1
            king_frequency = max(count.values())
            impostors = window_size - king_frequency
            
            # Shrink the window from the left if we are over budget
            while impostors > k:
                count[s[left]] -= 1
                left += 1
                
                # Recalculate stats for the shrunk window
                window_size = right - left + 1
                king_frequency = max(count.values())
                impostors = window_size - king_frequency
            
            # Record our maximum valid window size
            max_len = max(max_len, right - left + 1)
            
        return max_len