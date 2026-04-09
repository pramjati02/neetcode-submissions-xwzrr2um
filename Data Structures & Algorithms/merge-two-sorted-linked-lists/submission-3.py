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

        # exhaustive on both lists
        # does not stop iterating until all individual nodes in both lists have been iterated upon
        while curr1 or curr2: 
            if not curr1:
                node.next = curr2
                curr2 = curr2.next
            elif not curr2:
                node.next = curr1
                curr1 = curr1.next 
            else:
                if curr1.val <= curr2.val:
                    node.next = curr1
                    curr1 = curr1.next
                else:
                    node.next = curr2
                    curr2 = curr2.next
            node = node.next
        
            
        return dummy.next