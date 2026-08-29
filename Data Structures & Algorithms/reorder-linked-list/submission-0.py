# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = None
        second = slow.next
        slow.next = None
        curr = second


        while curr:
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt

        

        curr=head
    


        while temp:
           curr_next=curr.next
           temp_next=temp.next

           curr.next=temp
           temp.next=curr_next

           curr=curr_next
           temp=temp_next

        
