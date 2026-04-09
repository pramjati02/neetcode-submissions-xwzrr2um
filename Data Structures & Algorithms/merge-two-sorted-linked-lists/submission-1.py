class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        curr1 = list1
        curr2 = list2
        
        if not curr1:
            return curr2
        elif not curr2:
            return curr1

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node.next = curr1
                curr1 = curr1.next
            else:
                node.next = curr2
                curr2 = curr2.next
            node = node.next
        
        if curr1:
            node.next = curr1
        elif curr2:
            node.next = curr2
            
        return dummy.next