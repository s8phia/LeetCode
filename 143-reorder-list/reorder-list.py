class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Step 1: Find the middle using slow and fast pointers
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        slow.next = None  # Break the list into two halves

        # Step 3: Merge two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
