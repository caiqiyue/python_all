


class Father(object):
    f = 10
    def __init__(self) -> None:
        self.g = 100
        
    def test1(self):
        print("father",self)
        
    @classmethod
    def test2(cls):
        print("father",cls)
        
    @staticmethod
    def test3():
        print("test3")
        
        
class Children(Father):
    C = 10
    def __init__(self) -> None:
        """
        继承链：Children ---->  Father  ---->  object
        
        
        super考虑三个问题，用哪条继承链，找到继承链中 哪个节点的后一个节点，然后使用那后一个节点的方法，要传递什么参数
        super(Children,self)
        第一个参数，代表我需要找到 继承链中 children类的后一个节点
        第二参数代表，我是基于  child实例（children类）的继承链来找，如果这里填Father或者father类的实例，那就是在  Father ---->  object的继承链上，这个继承链没有children类
        同时，调用children类的后一个节点（Father类）的 init方法，第二个参数 self（child实例）会被当做init的参数传进去
        
        此外，super可以解决菱形继承时的 重复继承问题
        """
        # super(Children,self).__init__()
        super().__init__()#这种方式 只有在python3之后才可用,super()自动将自己存在的那个类（Children类），和存在于那个方法中（init的self参数）的第一个参数穿进去
        self.ch = 190
        
    def test4(self):
        print("children",self)
        
    @classmethod
    def test5(cls):
        """
        同时，super()第一个参数，最好不要写成 self.__class__，虽然这样是动态获取类，self或者cls并不稳定，会出现循环继承的问题出bug
        此外，super().init() 和 D.init(self)这两种不同方式不要混合使用
        
        """
        super(Children,cls).test2()#同样的方法，要找cls（children）继承链中，children节点的后一个节点的test2()方法，同时将cls作为参数传给test2()
        print("children",cls)
        
    @staticmethod
    def test6():
        print("test6")
        
        
child = Children()


print(child.__dict__)

Children.test5()
        
