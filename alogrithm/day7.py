
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
    
    def get(self,index):
        cur = self.head.next
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur.val
    
    def addAtHead(self,val):
        insert_node = ListNode(val=val)
        insert_node.next = self.head.next
        self.head.next = insert_node
        self.size += 1
        
    def addAtTail(self,val):
        insert_node = ListNode(val=val)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = insert_node
        self.size += 1
    
    def printLinkList(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next
    
    def addAtIndex(self,val,index):
        count = 0
        cur = self.head
        if index == self.size:
            self.addAtTail(val)
        if index > self.size:
            return None
        while count < index:
            cur = cur.next
            count += 1
        insert_node = ListNode(val)
        insert_node.next = cur.next
        cur.next = insert_node
        self.size += 1
    
    
    def deleteAtIndex(self,index):
        cur = self.head
        count = 0
        if index > self.size:
            return None
        while count < index:
            cur = cur.next
            count += 1
        cur.next = cur.next.next
        self.size -= 1
        
if __name__ == '__main__':
    mylinklist = MyLinkedList()
    mylinklist.addAtTail(0)
    mylinklist.addAtTail(1)
    mylinklist.addAtTail(2)
    mylinklist.addAtTail(3)
    mylinklist.addAtTail(4)
    mylinklist.addAtTail(5)
    mylinklist.printLinkList()
    # v = mylinklist.get(3)
    # print(v)
    # mylinklist.addAtIndex(10,2)
    # mylinklist.printLinkList()
    mylinklist.deleteAtIndex(5)
    mylinklist.printLinkList()