



def test():
    """
    test()是一个生成器，当他被创建的时候，不会被执行一点
    只有使用__next__或者 next()时，才会执行生成器函数，而且会在 yield处 将该函数挂起
    """
    res1 = yield 1
    print(res1)
    
    res2 = yield 2
    print(res2)
    
    
g = test()
# print(g.__next__())#开始执行到 yield 1,函数就被挂起，没有给res1赋值
# print(next(g))#从 yield 1 开始执行 给 res1赋值，运行到 yield 2 再次被挂起

print(g.send(None))#send()函数，会给上一次 函数被挂起的 yield的地方，给yield 赋值，所以 第一个 yield 被挂起的地方，它前面没有 yield了，所以不能不能穿一个非空值
print(g.send('333'))#给 yield 赋值，给 res1