class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the shelf
        result = []
        
        # Step 2: The Anchor Loop (leaves 2 spaces at the end)
        for i in range(len(nums) - 2):
            
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Launch your two friends
            left = i + 1
            right = len(nums) - 1
            
            # Step 4: The Pointer Dance
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum < 0:
                    left += 1  # Too small! Boost.
                elif total_sum > 0:
                    right -= 1  # Too big! Shrink.
                else:
                    # Target hit! Save the triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return result