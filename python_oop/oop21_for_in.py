class Person(object):
    
    def __init__(self) -> None:
        self.result = 1
        
    def __getitem__(self,item):
        if self.result >= 6:
            raise StopIteration("越界")
        self.result += 1
        return self.result
    
    def __iter__(self):
        self.result = 1#可以让 迭代器 多次使用
        """
        for in 遍历的时候，会找到 内置函数 而且 __iter__优先级 大于 __getitem__ 只要 有 __iter__就不会去 调用 __getitem__
        l = [1,2,3,4]
        iter(l)
        l 是 可迭代对象  里面 有  迭代器
        iter(l) 就是获取 l可迭代对象 内部的 迭代器  iter() 也是调用 内部的 __iter__ 内置函数  ，所以__iter__自定义的话必须要返回迭代器
        迭代器 是可以用 next()访问的 ，所以迭代器内部必须有 __next__和 __iter__ 内置函数
        """
        #return self  这样 会报错 因为 实例本身并不是迭代器  迭代器 要求内部 有 __next__内置函数 所以 再定义个__next__函数
        #return iter([1,2,3,4,5])
        return self#此时的实例中 有 next , self是迭代器  所以 不会报错
    def __next__(self):
        """
        如果不自定义 __next__  这个函数 就是 获取 到 iter返回的迭代器  self  然后 循环 使用 next(迭代器) 返回 结果
        """        
        if self.result >= 6:
            raise StopIteration("越界")
        self.result += 1
        return self.result
    
p = Person()


#for in  遍历的时候 调用 类内部 的 __getitem__这个函数
#并将这个 方法的 返回值 作为  for in遍历的  每次遍历的 值 而且必须注意到 函数内部的循环终止的条件

"""
for i in p  --->  iter(p) 调用 p内部的 __iter__ 返回 迭代器 -->  循环 next(迭代器) 返回值 赋给 i
此外 ，你不用 for in 去遍历  直接 next(p) 也可以 ，就不需要定义 __iter__ 也可以
所以 也可以 知道  可以被 next() 的未必是 迭代器 只要 有__next__就可以
迭代器 必须有 __iter__ 和 __next__，而且 迭代器 内部 的 next（）调用完之后，就不会被再调用

"""

#此时 的 迭代器 条件 未满足 （没有碰到 stop异常） 会 触发 next()
for i in p:
    print(i)

#此时 的 迭代器 中的 条件已经满足(碰到了 stop 异常) ，不会再触发 next（）了
#可以 在 __iter__中 把 条件置为 初始值 这样 又可以 next  了  可以让 迭代器 重复使用，否则就只能使用一次
for i in p:
    print(i)
    
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))#StopIteration: 越界