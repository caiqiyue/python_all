class Person(object):
    def __init__(self) -> None:
        self.cache = {}
        
    #索引操作，把实例对象可以当做 字典或者列表一样 进行索引 对值进行修改
    def __setitem__(self,key,value):
        self.cache[key] = value
        
        
    def __getitem__(self,key):
        return self.cache[key]
    
    
    def __delitem__(self,key):
        del self.cache[key]
        
        
p = Person()

p['name'] = 'caiqiyue'

print(p['name'])


del p['name']

print(p.cache)