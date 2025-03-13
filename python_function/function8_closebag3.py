



def outer():
    a = 1
    
    def inner():
        print(a)
        
    a = 2
    return inner


inner = outer()
inner()#2
"""
闭包的定义在 a =1后面， 在 a = 2 之前，为什么打印的是2？
在 inner没有执行之前，内部的变量a，仅仅当做变量标识存在，不会报错
当开始执行inner函数了，内部的变量a就会去找 a此时指向的值是多少
那么我们是在第16行执行的inner函数，此时的a = 2，所以打印2
"""


def test():
    funcs = []
    for i in range(1,4):
        def test2():
            print(i)
        funcs.append(test2)
    return funcs

funcs = test()

print(funcs)

"""
这个和上面的例子，同一个道理，在没有执行test2之前，内部的i仅当做变量标识，只有执行时才会去找此时的i指向什么值，指向3
"""
funcs[0]()#3
funcs[1]()#3
funcs[2]()#3

def ceshi():
    funcs = []
    for i in range(1,4):
        def ceshi2(num):
            """
            ceshi2(num)，使用num接收 i 
            就相当于在 ceshi2的内部定义了 num = i
            然后定义了内部函数 ceshi3，ceshi3打印 外部变量num，所以 num + ceshi3就是一个新闭包
            """
            def ceshi3():
                print(num)
            return ceshi3
        funcs.append(ceshi2(i))
    return funcs

c = ceshi()
c[0]()
c[1]()
c[2]()

