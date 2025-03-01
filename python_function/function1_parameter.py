
"""
* args 我们输入 1,2,3,4 但是到函数内部就变成了 (1,2,3,4) 这就是将多个形参装包
** kwargs 我们输入 a=1,b=2, 到函数内部就变成了 {a:1,b:2},  这就是将 关键字参数装包
同样，有装包，就有解包
*(1,2,3,4) --->  1,2,3,4
**{a:1,b:2}   ---->  a=1,b=2
"""
def args_app(a,b,c,d):
    print(a,b,c,d)
    
def kwargs_app(a,b):
    print(a,b)

def kwargs_app2(a,c):
    print(a,c)



def pFunc():
    print("这是一个函数")
    
def numberSum(a,b):
    print(a + b)
    

def numberSet(*args):
    print(args,type(args))
    print(*args)#拆包
    args_app(*args)# 相当于  args_app(1,2,3,4)
    
    # for i in args:
    #     print(i)
        
def numberDict(**args):
    print(args,type(args))
    # print(**args)#这是在 拆包，但是无法打印，因为 字典拆包后，会拆成关键字参数 a=1,b=2，而print函数中，没有形参a和b
    kwargs_app(**args)#相当于  kwargs_app(a=1,b=2)
    try:
        kwargs_app2(**args)# kwargs_app2(a=1,b=2),但是 形参是 a  和  c，这就会报错 got an unexpected keyword argument 'b'
    except Exception as e:
        print(e)
        
def hit(body='caiqiyue'):#这个称为 缺省参数，有默认值，另外就是 缺省参数必须得写在形参后面
    print(body)
    
        

pFunc()#加上括号是执行该函数，不加括号，返回一个函数体对象

numberSum(a = 1,b=3)#可以 a = 1这种叫关键字参数，也可以（1，3）实参1和3，与形参一一对应

numberSet(1,2,3,4)#不定长参数，*args，将多个实参输入，统一到一个元组中

numberDict(a = 1,b = 2)#不定长参数，**args，将关机字参数输入，统一到一个字典中

hit()