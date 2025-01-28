#24. Swap Nodes in Pairs

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    curr = dummy

    while curr.next and curr.next.next:
        temp1 = curr.next
        temp2 = curr.next.next

        temp1.next = temp2.next
        temp2.next = temp1
        curr.next  = temp2
        curr = temp1
        
    return dummy.next
