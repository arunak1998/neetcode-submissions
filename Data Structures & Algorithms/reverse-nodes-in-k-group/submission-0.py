# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findkthnode(temp,k):

            curr=temp

            while curr and k>1:
                curr=curr.next
                k-=1

            return curr
        temp=head
        prevnode=None
        nextNode=None


        while temp:

            kthNode=findkthnode(temp,k)

            if not kthNode:

                if prevnode:
                    prevnode.next=temp

                break
            
            nextnode=kthNode.next
            kthNode.next=None

            newnode=None
            curr=temp
            while curr:
                nxt=curr.next
                curr.next=newnode
                newnode=curr
                curr=nxt


            if temp==head:
                head=kthNode
            else:
                prevnode.next=kthNode

            prevnode=temp
            temp=nextnode
        return head

            



       