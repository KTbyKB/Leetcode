#19 Remove nth Node From End Of List
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return head
    p1 = p2 = head
    for i in range(n):
         p2 = p2.next
    if not p2:
        return head.next
    while p2 and p2.next :
        p1 = p1.next
        p2 = p2.next
    p1.next = p1.next.next
    return head
