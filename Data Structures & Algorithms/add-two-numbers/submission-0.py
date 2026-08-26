# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        


        curr=l1
        curr2=l2
        resNode=ListNode()

        temp=resNode
        carry=0

        while curr or curr2 or carry:

            n1=curr.val if curr else 0

            n2=curr2.val if curr2 else 0

            val=n1+n2+carry
            carry=val//10
            val=val %10
            temp.next=ListNode(val)
            temp=temp.next

            curr=curr.next if curr else None
            curr2=curr2.next if curr2 else None

        return  resNode.next

        