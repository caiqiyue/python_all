



#获取一个装饰器
def getDecorator(c,l):
    #装饰器
    def decorator(func):
        #被装饰的函数
        def function_decorated(*args,**kwargs):
            #新添加的逻辑
            print(c * l)
            #原函数
            res = func(*args,**kwargs)
            return res
        return function_decorated
    return decorator

@getDecorator('*',20)  #decorator = getDecorator('-',10)  ----->  test1 = decorator(test1)
def test1(num):
    return num

@getDecorator('-',2)
def test2(num1,num2):
    print(num1 + num2)
    
res1 = test1(10)
print(res1)


res2 = test2(12,100)
print(res2)