class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
        


class MyLinkList(object):
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        
    def printLinkList(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next
            
    def addItemAtTail(self,val):
        will_insert = ListNode(val=val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = will_insert     
        self.size += 1
    
    def addItemAtHead(self,node):
        # if isinstance(node,ListNode):
        #     return None
        node.next = self.head.next
        self.head.next = node   
        self.size += 1
            
    def reverseLinkList(self):
        """
        断头连接
        """
        if self.size == 0:
            return None
        s = self.head.next
        p = s.next
        self.head.next = None
        while p is not None:
            self.addItemAtHead(s)
            s = p
            p = s.next
        return self.head
    
    def reverse(self):
        """
        双指针法
        """
        if self.size == 0:
            return None

        pre = None
        cur = self.head.next
        
        self.head.next = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head.next = pre
        return self.head
    
    def reverse_recur(self,cur,pre):
        if cur is None:
            return pre

        tmp = cur.next
        cur.next = pre
        return self.reverse_recur(tmp,cur)   
    
    def reverse_use_recur(self):
        """
        使用递归形式完成双指针
        """
        cur = self.head.next
        pre = None
        self.head.next = None
        reverse_head = self.reverse_recur(cur,pre)
        self.head.next = reverse_head
        return self.head
    
if __name__ == '__main__':
    mylinklist = MyLinkList()
    mylinklist.addItemAtTail(0)
    mylinklist.addItemAtTail(1)
    mylinklist.addItemAtTail(2)

    mylinklist.printLinkList()
    mylinklist.reverse_use_recur()
    mylinklist.printLinkList()