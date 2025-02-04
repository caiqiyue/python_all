


import functools



@functools.total_ordering
class Person(object):
    
    def __eq__(self, value: object) -> bool:
        print("这是 等于  号  的内置函数")
        return True
        
    def __lt__(self,other):
        print("这是小于 的 内置函数")
        
    def __bool__(self):
        return False
        
        
p1 = Person()
p2 = Person()

#我们并没有定义 小于等于  的内置函数  而是装饰器 帮我们 调用了 等于 和 小于 这两个内置函数
#我们在  等于  内置函数 中  返回 True 那么 <=  一定是 满足的 所有 也必定返回 True
print(p1 <= p2)#True


#'__gt__': <function _gt_from_lt at 0x00000299ACCDA0D0>, '__le__': <function _le_from_lt at 0x00000299ACCDA160>, '__ge__': <function _ge_from_lt at 0x00000299ACCDA1F0>
print(Person.__dict__)
#可以发现 ，我们只定义了  等于 和 小于  但是  装饰器 帮助我们 根据 定义好的两个函数 去 拓展出了 剩余的所有函数


#有时候 ，没有 比较运算  满足 ‘非空即真’,  本质上 这个时候 调用的时  __bool__内置函数
if 1:
    print("True")
    
if 'xxx':
    print('True')
    
if not p1:#本应该是  True  因为非空即真  但是  修改__bool__函数 返回  false 
    print("False")




