# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        curr=head
        i=0

        while curr:
        

            curr=curr.next

            i+=1
        removeIndex=i-n

        if removeIndex==0:
            return head.next

        curr=head

        for j in range(i-1):

            if j+1==removeIndex:
                curr.next=curr.next.next

                break
            curr=curr.next
        return head
