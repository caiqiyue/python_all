
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
class MyLinkList(object):
    def __init__(self):
        self.head = ListNode(0)
        self.next = None
        
    def printList(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next
            
    def addAtTail(self,val):
        insert_node = ListNode(val)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = insert_node
        
    def reverse(self):
        cur = self.head
        while cur.next is not None and cur.next.next is not None:
            tmp1 = cur.next
            tmp2 = tmp1.next.next
            
            cur.next = cur.next.next
            cur.next.next = tmp1
            tmp1.next = tmp2
            
            cur = cur.next.next
        return self.head
    
    
if __name__ == '__main__':
    mylinklist = MyLinkList()
    mylinklist.addAtTail(0)
    mylinklist.addAtTail(1)
    mylinklist.addAtTail(2)
    mylinklist.addAtTail(3)
    # mylinklist.addAtTail(4)
    mylinklist.printList()
    mylinklist.reverse()
    mylinklist.printList()