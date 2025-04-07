"""
判断链表中是否有环
"""


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
        
    def createCircle(self,val_list,start):
        cur = self.head
        self.size = len(val_list)
        for num in val_list:
            insert_node = ListNode(val=num)
            if num == val_list[start]:
                start_node = insert_node
            cur.next = insert_node
            cur = cur.next
        cur.next = start_node
        return self.head

        
    def printList(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next
    
    def hasCircle(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                index1 = slow
                index2 = self.head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1.val
        #如果没有环，一定有Null
        return None
            
if __name__ == '__main__':
    nums = [0,1,2,3,4,5]
    mylinklist = MyLinkList()
    mylinklist.createCircle(nums,2)
    
    rs = mylinklist.hasCircle()
    print(rs)