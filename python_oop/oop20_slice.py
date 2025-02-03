class Person(object):
    
    def __init__(self) -> None:
        self.items = [1,2,43,5,5,67,7,3,2,5,54]
    
    def __setitem__(self,key,value):
        # print(key,value)
        # print(key.start,key.stop,key.step)#打印  关于 切片的三要素  开始  结束  步长
        if isinstance(key,slice):
            self.items[key] = value
        
    def __getitem__(self,item):
        #return item#一个切片对象
        if isinstance(item,slice):#判断是否是 切片对象  以防和索引操作搞混
            return self.items[item]
    
    def __delitem__(self,key):
        if isinstance(key,slice):
            del self.items[key]
            
p = Person()

p[0:4:2] = [1,23]#slice(0, 4, 2) slice是切片对象  里面 包含 start,stop ,step三个属性    [1, 23, 4]  是value值

print(p[0:4:2])

print(p.items)
del p[0:1]
print(p.items)