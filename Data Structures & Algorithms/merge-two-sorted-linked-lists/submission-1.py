# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr1 = list1
        curr2 = list2
        tail = None

        while curr1 and curr2:
            if curr1.val < curr2.val:
                node = curr1
                curr1 = curr1.next
            else:
                node = curr2
                curr2 = curr2.next

            if res is None:
                res = node
                tail = node
            else:
                tail.next = node
                tail = node

        if curr1:
            if res is None:
                res = curr1
            else:
                tail.next = curr1

        if curr2:
            if res is None:
                res = curr2
            else:
                tail.next = curr2

        return res