

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
class MyLinkList(object):
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def addAtTail(self,val):
        tail = self.head
        while tail.next is not None:
            tail = tail.next
            
        insert_node = ListNode(val)
        tail.next = insert_node
        self.size += 1
        
    def printList(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next
            
    def removeElement(self,n):
        slow = self.head
        fast = self.head
        if n > self.size:
            return None
        
        while n + 1 > 0 and fast is not None:
            fast = fast.next
            n -= 1
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return self.head
    
if __name__ == '__main__':
    mylinklist = MyLinkList()
    mylinklist.addAtTail(0)
    mylinklist.addAtTail(1)
    mylinklist.addAtTail(2)
    mylinklist.addAtTail(3)
    mylinklist.addAtTail(4)
    mylinklist.addAtTail(5)
    mylinklist.printList()
    print("===================================")
    mylinklist.removeElement(2)
    mylinklist.printList()