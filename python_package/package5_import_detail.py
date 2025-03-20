import Tool
"""
1.第一次导入 Tool 模块的时候，会在 Tool 的命名空间中，执行一遍自身的代码（注意是在自己的命名空间中，也就是自己的文件内部）
*无论是 （import *） 还是（from . import 某一个资源） 都会让模块自身全部执行一遍，所以两种导入方式，占内存是一样的

2.执行完自身的代码之后，就会创建一个  模块对象  属于module类， 它会把这个模块内的所有资源作为属性绑定在 创建的模块对象上 模块对象的名称就是模块名称
3.import other 仅仅是有使用权，（而且只是导入到当前的命名空间）因为这个other 就是一个变量名，指向了 那个被创建的 模块对象，就可以使用 对象.属性， 去使用模块内的资源了

def test():
    import other
    print(other.num)
print(other) 在局部作用域（函数的命名空间中导入），在外部无法使用
"""
print(Tool)
print(id(Tool))
print(type(Tool))
print(Tool.__dict__)

print(Tool.num)