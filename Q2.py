class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
#         right = head+2
#         right = head+n
        right = head
        
#         while n is greater than 0 and right is not null we will keep shifting right
        while n>0 and right:
            right = right.next
#             Once n = 0 that means we shifted by the amount that we wanted to shift by
            n-=1
#         Keep shifting both pointers until right reaches the end of the list    
        while right:
            left = left.next
            right = right.next
            
        #deleting
        left.next = left.next.next
        return dummy.next