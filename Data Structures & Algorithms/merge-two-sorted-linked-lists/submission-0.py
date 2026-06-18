# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        # 2. THE GAME LOOP: Compare the fronts of both piles as long as both have blocks
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1      # Snap Pile 1 block to our train
                list1 = list1.next     # Move our eyes to the next block in Pile 1
            else:
                tail.next = list2      # Snap Pile 2 block to our train
                list2 = list2.next     # Move our eyes to the next block in Pile 2
                
            tail = tail.next           # Move our tail worker to the new end of the train
            
        # 3. CLEAN-UP: One pile is empty. Snap the whole remaining pile to the tail instantly
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
            
        # 4. FINALE: Return the finished list, skipping our fake starting box
        return dummy.next