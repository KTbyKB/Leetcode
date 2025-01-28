#2. Add Two Numbers
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    carry = 0
    curr = dummy

    while l1 or l2:
        if l1:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0
        if l2:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0
            
        s = val1 + val2 + carry

        curr.next = ListNode(s % 10)
        curr = curr.next
        carry = s // 10

    if carry:
        curr.next = ListNode(carry)
    return dummy.next
        return dummy.next
