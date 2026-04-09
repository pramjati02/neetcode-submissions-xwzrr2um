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

        # Iterates until all individual nodes in one list has been exhausted
        # from which it breaks out of the loop
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node.next = curr1
                curr1 = curr1.next
            else:
                node.next = curr2
                curr2 = curr2.next
            node = node.next
        
        # Checks: if there are still any nodes in either list (curr1, curr2)
        # pick up from the node where we left off from the loop
        # add the rest of the nodes to the merged list 
        # IMPORTANT: CONSIDERS ALL NODES IN THE LIST AT ONE OUTSIDE LOOP, NOT INDIVIDUAL NODES
        if curr1:
            node.next = curr1
        elif curr2:
            node.next = curr2
            
        return dummy.next