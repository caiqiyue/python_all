
#生成器的创建方式1
l = (i for i in range(10) if i % 2 != 0)
#生成器表达式，用圆括号，用方括号就是列表推导式 
print(l)

print(next(l))

print(l.__next__())

for i in l:
    print(i)
    
    

#生成器的创建方式2
"""
yield 可以阻断函数执行，当执行到 yield 返回值，并记录当前状态；只有使用next() 或者 __next__可以让其继续执行，直到再次遇到yield
yield 1  1就是状态
"""
def test():
    yield 1
    print(1)
    
    yield 2
    print(2)
    
    yield 3
    print(3)


def test2():
    for i in range(1,10):
        yield i

#迭代器和生成器一样，都可以使用next和for in来
s = test2()
for item in s:
    print(item)


g = test()
print(g)
print(next(g))
print(next(g))


    
    