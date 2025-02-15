class Person(object):
    
    # def __new__(cls):
    #     print("新建对象过程时，会触发new函数，但被我拦截了")
        
    def __init__(self) -> None:
        self.age = 10
        
    def __del__(self):
        print("这个实例被释放了")
        
"""
创建一个 对象时 调用 new方法，会返回给 init一个实例对象
初始化对象一些数据时 ，调用 init方法，接收来自  new方法的结果 
当对象被释放时 调用 del方法
"""
        
p = Person()

print(p)#原本的 实例p会被分配内存 通过 new函数   ，但现在我修改了 new
print(p.age)

