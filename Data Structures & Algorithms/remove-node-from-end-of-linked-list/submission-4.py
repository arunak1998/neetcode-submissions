# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        length=0

        curr=head
        while curr:
            length+=1
            curr=curr.next
        
        if n==length:
            head=head.next
            return head

        i=0

        curr=head

        while curr and curr.next:

            if (length-i)-1==n:
                curr.next=curr.next.next
                break

            else:
                curr=curr.next

            i+=1
        return head