# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Find out if the last element in the list points to another element within the list
        # If it does, return True. 
        # If the last element does not point to an element within the list, return False
        li = []
        while head:
            if head in li:
                return True
            li.append(head)
            head = head.next

        return False

        