


def test(a,b):
    print(a + b)
    



#函数本身也是一个对象，函数体存在内存当中，函数名作为一个变量，保存函数体的内存地址
#变量就可以赋值
test2 = test
"""
给函数的形参传递值，本质上也是 给 形参赋值
如果给形参一个函数，那么这个形参接收到函数的函数 就是 高阶函数
"""

#比如sorted就是一个高阶函数

l = [{"name":'cac','age':10},{'name':'caiqiyue','age':12}]
def getKey(x):
    return x['age']

#形参 接受一个 函数 
sorted_l = sorted(l,key=getKey)#以age排序
print(sorted_l)

#简单的场景

def calculate(a,b,func):
    print(func(a,b))
    
    
a = 10
b = 12

def add_number(a,b):
    return a + b 
def minus_number(a,b):
    return a - b 

calculate(a,b,add_number)