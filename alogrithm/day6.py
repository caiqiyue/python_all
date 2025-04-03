

class Node(object):
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class NodeList(object):
    def __init__(self,head):
        self.head = head

    def CreateNodeList(self,nums):
        s = self.head
        for num in nums:
            insert_node = Node(val=num)
            s.next = insert_node
            s = s.next
        return self.head
    
    def PrintNodeList(self):
        s = self.head.next
        nums = []
        while s is not None:
            nums.append(s.val)
            s = s.next
        print(nums)
    
    def RemoveTarget(self,target):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == target:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head

class NodeListWithoutDummyHead(object):
    def __init__(self,nums):
        self.head = Node(val=nums[0])
        insert_node = self.head
        for i in range(1,len(nums)):
            insert_node.next = Node(val=nums[i])
            insert_node = insert_node.next
    
    def PrintNodeList(self):
        cur = self.head
        nums = []
        while cur is not None:
            nums.append(cur.val)
            cur = cur.next
        print(nums)
    
    def RemoveTarget(self,target):
        if self.head.val == target:
            self.head = self.head.next
        cur = self.head
        while cur.next is not None:
            if cur.next.val == target:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head            

    
if __name__ == '__main__':

    nums = [1,2,3,4,5,6,7]
    nodelist = NodeListWithoutDummyHead(nums)
    nodelist.PrintNodeList()
    nodelist.RemoveTarget(3)
    
    nodelist.PrintNodeList()