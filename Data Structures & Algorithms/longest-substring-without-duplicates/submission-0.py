class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in (range(len(s))):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])


            current_window_size = right - left + 1
            if current_window_size > max_len:
                max_len = current_window_size

        return max_len
