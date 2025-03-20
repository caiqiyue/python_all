




a = 999

def test():
    """
    在test内部的变量a，会先从函数内部去找，找不到，再去全局变量找
    """
    global a  # 如果要将 局部变量申明为 全局变量 需要 global 关键字
    a = 100
    print(a)
    
def test2():
    """
    test3属于 local 区域，那么 test2就是 E 区域，test3是test2的闭包，变量的查找顺序
    就是先从test3 --- > test2 ---->  本py文件  ----->  内建模块
    """
    a = 10
    print(a)
    def test3():
        nonlocal a # 此时将 local区域的 变量  声明为 E区域的变量 使用 nonlocal 这样 a = 11 修改的就是test2()内部的 变量a
        a = 11#
        print(a)
    test3()
    
"""
而且需要注意的是，python的声明顺序，和执行顺序


def test()
    print(a)
a = 3
test()是可以执行的，尽管函数是在 a =3 之前定义，但是 只有在函数执行的时候，才会去找函数内部变量a的值
"""

test2()
