# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head 
        length = 0 

        while curr: 
            stack.append(curr)
            curr = curr.next
            length+=1
        
        curr = head 
        length = length//2
        
        while length!=0:
            nxt = curr.next 
            node = stack.pop()
            curr.next = node 
            node.next = nxt
            curr = nxt 
            length-=1

        curr.next = None
        #curr = head
        
        