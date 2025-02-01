

from typing import Any


class Person:
    #这个内置函数，主要是用于  在给  设置或者 修改  实例属性的时候 起到作用
    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'age' and name in self.__dict__.keys():#判断是不是第一次创建实例属性
            print("只读属性不能修改")
        else:
            self.__dict__[name] = value
            #self.name = value这样是死循环，千万不能这么写。因为self.name = value的时候又是在创建实例属性，又会调用这个setattr
        
        
p = Person()
#第一次创建只读属性
p.age = 10
"""
创建或者修改实例属性的时候，就会自动调用setattr这个内置方法，
先判断，如果是第一次创建实例属性，则允许
如果是修改这个只读属性，则不允许，对于setattr，只要什么都不做，就不会把你要修改的值在dict中去修改
"""
print(p.__dict__)#创建成功，存储到dict中去了


#第二次修改只读属性
p.age = 999
print(p.__dict__)#修改操作被拦截了

"""
只读属性实现的第一种方式，我们仍然可以  通过  _类名__实例属性 这样修改只读属性，或者直接通过dict修改
只读属性的第二种方式，不使用property来修饰，用 setattr在创建或者修改只读属性的时候进行额外操作
这样的话，就不存在  _类名__实例属性   这样来修改只读属性，但是 dict的防范仍然能修改，毕竟python只是伪私有

"""





