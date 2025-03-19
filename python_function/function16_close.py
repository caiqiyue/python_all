


def test():
    """
    注意 return 和 yield 不一样，一个是终止函数，一个是 挂起函数，记录当前执行到的位置
    在生成器中，如果遇到 return语句会直接触发stopiteration异常
    """
    yield 1
    print('a')
    
    yield 2
    print('b')
    
    yield 3
    print('c')
    

g = test()
print(g.__next__())
print(g.__next__())
g.close()#关闭生成器，只想要前两个值，不想要后面的值话，可以关闭它，本质上就是将状态值移到最后一位，这样就会触发 stopiteration异常，阻止其继续迭代
print(g.__next__())



#而且生成器只能使用一次，全部迭代完一次后，在迭代就没有值了
for i in g:
    print(i)

for i in g:
    print(i)


