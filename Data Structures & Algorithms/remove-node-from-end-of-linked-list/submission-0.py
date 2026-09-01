class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        count = -n

        while start:
            count += 1
            start = start.next

        # 删除 head
        if count == 0:
            return head.next

        start = head

        while count > 1:
            count -= 1
            start = start.next

        start.next = start.next.next

        return head