from typing import Any


class Person(object):
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        #让一个实例对象，可以像函数一样去使用（函数的本质也是个对象嘛）
        print("xxxxx",args,kwds)
        

p = Person()

p(123,435,name='caiqiyue')


"""
__call__方法的应用场景，类似与  偏函数  ，一个函数中  偏爱某一个参数

比如说 现在有一个需求，需要创建多只画笔 ，画笔 有两个 构成  材料 和  颜色
材料 只有两种  钢笔和铅笔  颜色 有十几种甚至更多，那么画笔的材料相比于颜色是比较稳定的，所以就是  偏函数  偏爱  材料

"""
#第一种方法 创建 画笔（显然，重复性太高，用函数来封装，减少重复）
print("创建了一只{}，颜色是{}".format('钢笔','红色'))
print("创建了一只{}，颜色是{}".format('铅笔','橘色'))
print("创建了一只{}，颜色是{}".format('钢笔','黑色'))
print("创建了一只{}，颜色是{}".format('钢笔','白色'))
print("创建了一只{}，颜色是{}".format('钢笔','绿色'))
print("创建了一只{}，颜色是{}".format('铅笔','黄色'))
print("创建了一只{}，颜色是{}".format('铅笔','青色'))


#第二种方法，创建  画笔（的确，比第一种方法重复性减少，但是 画笔类型这个参数 总共就两个选择 ，每次创建的时候 还要输入这个参数 怪麻烦的  ）
def createPen(p_color,p_type):
    print("创建了一只{}，颜色是{}".format(p_type,p_color))
    
createPen('钢笔','红色')
createPen('铅笔','绿色')
createPen('钢笔','黄色')


#第三种方式，使用偏函数   可以把 笔的类型 先设置好  ，不同笔的类型 生成一个专门的  创建画笔的  函数
import functools
gangbiCreator = functools.partial(createPen,p_type='钢笔')
gangbiCreator('红色')
gangbiCreator('白色')
qianbiCreator = functools.partial(createPen,p_type='铅笔')
qianbiCreator('绿色')
qianbiCreator('黑色')


#把这个偏函数  应用到 面向对象中 __call__方法实现

class PenFactory(object):
    def __init__(self,p_type) -> None:
        self.p_type = p_type
        
    def __call__(self,p_color) -> Any:
        print("创建一只画笔，材质是{}，颜色是{}".format(self.p_type,p_color))
        
gangbi = PenFactory('钢笔')
gangbi("红色")
gangbi("黑色")
gangbi("绿色")

qianbi = PenFactory('铅笔')
qianbi('黄色')




