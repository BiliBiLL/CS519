"""
 Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
          
         
         
class Solution(object):
    def build(self,node,s):
        cur = node
        for x in s:
            cur.next = ListNode(x)
            cur = cur.next
            
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:return False
        slow,fast = head,head
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            if slow == fast:return True
        return False
            
            
            
            
if __name__ == "__main__":
    node = ListNode(1)
    s = [2,3,4]
    cls = Solution()
    cls.build(node,s)
    print node.val,node.next.val,node.next.next.val,node.next.next.next.val
    
    print cls.hasCycle(node)
    
"""
Note, this problem us two pointers, fast move one and slow move one, in case they will meet with each other. 
The most time comsume place is debug, happend mostly in line 28,30. how to avoid NoneType don't have next attribute.
"""
    
