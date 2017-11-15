# 

#         self.next = None
class Node:
    def __init__(self, item):
        self.data=item
        self.next=None

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast.next!=None:
            slow=slow.next
            if fast.next!=None:
                fast=fast.next.next
            if fast is slow:
                return True
        return False


#if __name__=="__main__":
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=head.next
print (Solution().hasCycle(head))
