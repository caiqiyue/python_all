
"""
计算（2 + 6 - 4） * 5 = 20
"""

#代码1,面向过程
# def add(a,b):
#     return a + b

# def multiply(a,b):
#     return a * b

# def minus(a,b):
#     return a - b

# def division(a,b):
#     return a / b

# r1 = add(2,6)
# r2 = minus(r1,4)
# r3 = multiply(r2,5)
# print(r3)

#代码2，面向过程，简化
# result = 0
# def first_value(n):
#     global result
#     result = n

# def add(n):
#     global result
#     result += n

# def minus(n):
#     global result
#     result -= n
    
# def multiply(n):
#     global result
#     result *= n
    
# def division(n):
#     global result
#     result /= n
    
# first_value(2)
# add(6)
# minus(4)
# multiply(5)
# print(result)

#代码3 面向对象
# class Calculator(object):
#     __result = 0
    
#     @classmethod
#     def first_value(cls,v):
#         Calculator.__result = v
    
#     @classmethod
#     def add(cls,v):
#         Calculator.__result += v
        
#     @classmethod
#     def minus(cls,v):
#         Calculator.__result -= v
    
#     @classmethod
#     def multiply(cls,v):
#         Calculator.__result *= v
        
#     @classmethod
#     def division(cls,v):
#         Calculator.__result /= v
        
#     @classmethod
#     def show(cls):
#         print(cls.__result)
        
# Calculator.first_value(2)
# Calculator.add(6)
# Calculator.minus(4)
# Calculator.multiply(5)
# Calculator.show() 

#代码4 面向对象

# class Calculator(object):
    
#     def __init__(self,num) -> None:
#         self.__result = num
        
#     def add(self,n):
#         self.__result += n
        
#     def minus(self,n):
#         self.__result -= n
        
#     def multiply(self,n):
#         self.__result *= n
        
#     def division(self,n):
#         self.__result /= n
        
#     def show(self):
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()

#代码5，面向对象，加上错误检查

# class Calculator(object):
    
#     def __init__(self,n) -> None:
#         self.check_num(n)
#         self.__result = n
    
#     def check_num(self,num):
#         if not isinstance(num,int):
#             raise TypeError("not int")
    
#     def add(self,n):
#         self.check_num(n)
#         self.__result += n
        
#     def minus(self,n):
#         self.check_num(n)
#         self.__result -= n
        
#     def multiply(self,n):
#         self.check_num(n)
#         self.__result *= n
        
#     def division(self,n):
#         self.check_num(n)
#         self.__result /= n
        
#     def show(self):
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()

#代码6 面向对象  装饰器
# class Calculator(object):
    
#     #装饰器
#     def check_num_decorator(func):#传入 需要被装饰 的函数
#         def inner(self,n):#内部实现 闭包
#             if not isinstance(n,int):#需要新加的逻辑流程
#                 raise TypeError("not int")
#             return func(self,n)#返回，并执行原来的函数
#         return inner#返回闭包
    
#     @check_num_decorator
#     def __init__(self,n) -> None:
#         self.__result = n
    
#     @check_num_decorator
#     def add(self,n):
#         self.__result += n
#     @check_num_decorator
#     def minus(self,n):
#         self.__result -= n
        
#     @check_num_decorator
#     def multiply(self,n):
#         self.__result *= n
        
#     @check_num_decorator
#     def division(self,n):
#         self.__result /= n
        
#     def show(self):
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()

#代码7，装饰器的私有化  不让外界使用装饰器
# class Calculator(object):
    
#     #装饰器
#     def __check_num_decorator(func):#传入 需要被装饰 的函数
#         def inner(self,n):#内部实现 闭包，且需要保证 inner传递的参数 和 被装饰的func 需要传递 参数 保持一致
#             if not isinstance(n,int):#需要新加的逻辑流程
#                 raise TypeError("not int")
#             return func(self,n)#返回，并执行原来的函数
#         return inner#返回闭包
    
#     @__check_num_decorator
#     def __init__(self,n) -> None:
#         self.__result = n
    
#     @__check_num_decorator
#     def add(self,n):
#         self.__result += n
#     @__check_num_decorator
#     def minus(self,n):
#         self.__result -= n
        
#     @__check_num_decorator
#     def multiply(self,n):
#         self.__result *= n
        
#     @__check_num_decorator
#     def division(self,n):
#         self.__result /= n
        
#     def show(self):
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()

#代码8 加入 识别字符串，并发声

# import win32com.client

# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # speaker.Speak('我的名字是蔡启越')

# class Calculator(object):
#     """
#     实例.方法
#     类.方法
#     都会自动地往方法中传入self或者cls
#     """
    
#     #装饰器
#     def __check_num_decorator(func):#传入 需要被装饰 的函数
#         def inner(self,n):#内部实现 闭包
#             if not isinstance(n,int):#需要新加的逻辑流程
#                 raise TypeError("not int")
#             return func(self,n)#返回，并执行原来的函数
#         return inner#返回闭包
    
#     @__check_num_decorator
#     def __init__(self,n) -> None:
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('{}'.format(n))
#         self.__result = n
    
#     @__check_num_decorator
#     def add(self,n):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('加{}'.format(n))
#         self.__result += n
#     @__check_num_decorator
#     def minus(self,n):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('减{}'.format(n))
#         self.__result -= n
        
#     @__check_num_decorator
#     def multiply(self,n):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('乘以{}'.format(n))
#         self.__result *= n
        
#     @__check_num_decorator
#     def division(self,n):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('除以{}'.format(n))
#         self.__result /= n
        
#     def show(self):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak('等于{}'.format(self.__result))
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()

#代码9  语音发送 装饰器

# import win32com.client

# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # speaker.Speak('我的名字是蔡启越')

# class Calculator(object):
#     """
#     (1) 实例.方法
#         类.方法
#         都会自动地往方法中传入self或者cls
#     (2)
#         装饰器是可以嵌套的
#         在最上面的装饰器，先执行
        
#         看我们的两个装饰器，都是先执行 新的逻辑，再执行 被装饰的函数
#         应该是先判断输入的数 是否 是 整数，再去播报
        
#         所以 是 result操作，被  播报 装饰，  （result操作 + 播报）被 int类判断装饰
        
#         但是 show函数，因为 形参的结构不同，无法使用现在设计的装饰器
        
#         被装饰的函数，都会从  原函数 变成 inner 函数 ，因为 装饰器 return 的 是 inner
    
#     """
#     def __say_decorator(func):
#         def inner(self,n):
#             speaker = win32com.client.Dispatch("SAPI.SpVoice")
#             speaker.Speak(n)
#             return func(self,n)
        
#         return inner
    
#     #装饰器
#     def __check_num_decorator(func):#传入 需要被装饰 的函数
#         def inner(self,n):#内部实现 闭包
#             if not isinstance(n,int):#需要新加的逻辑流程
#                 raise TypeError("not int")
#             return func(self,n)#返回，并执行原来的函数
#         return inner#返回闭包
    
#     @__check_num_decorator
#     @__say_decorator
#     def __init__(self,n) -> None:
#         self.__result = n
    
#     @__check_num_decorator
#     @__say_decorator
#     def add(self,n):
#         self.__result += n
        
        
#     @__check_num_decorator
#     @__say_decorator
#     def minus(self,n):
#         self.__result -= n
        
#     @__check_num_decorator
#     @__say_decorator
#     def multiply(self,n):
#         self.__result *= n
        
#     @__check_num_decorator
#     @__say_decorator
#     def division(self,n):
#         self.__result /= n
        
#     def show(self):
#         print(self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()


#代码10 装饰器生成器

# import win32com.client

# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # speaker.Speak('我的名字是蔡启越')

# class Calculator(object):
#     """
#     装饰器，只能接受 func 被装饰函数，因为这是 系统自动的  add = __say_decorator(add)
#     装饰器内部的 inner 函数的参数 必须和 被装饰函数 的 形参 一致
#     所以 装饰器 和 闭包 inner 的 形参 都固定或者说 受到限制，不灵活
    
#     """

    
    
#     def __say_decorator_generator(say_word=""):
#         """
#         这就是装饰器生成器
#         内部是一个装饰器，return 该装饰器
        
#             say_decorator = __say_decorator_generator(say_word) 装饰器生成器，返回一个 装饰器
#             通过 不同的 say_word 创建了 不同的适合各个函数 的装饰器
    
#       @__say_decorator_generator(say_word) 本质上是一个装饰器
#        def ....
#         """
#         def __say_decorator(func):
#             def inner(self,n):
#                 self.__say_word(say_word,n)# 把语音播报的实现过程 封装起来，需要改动该语音实现过程的话，只需要改一个地方
#                 return func(self,n)
#             return inner
#         return __say_decorator
    
#     #装饰器
#     def __check_num_decorator(func):#传入 需要被装饰 的函数
#         def inner(self,n):#内部实现 闭包
#             if not isinstance(n,int):#需要新加的逻辑流程
#                 raise TypeError("not int")
#             return func(self,n)#返回，并执行原来的函数
#         return inner#返回闭包
    
#     @__check_num_decorator
#     @__say_decorator_generator()
#     def __init__(self,n) -> None:
#         self.__result = n
        
#     def __say_word(self,say_word,n):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak(say_word + str(n))
    
#     @__check_num_decorator
#     @__say_decorator_generator('加')
#     def add(self,n):
#         self.__result += n
        
        
#     @__check_num_decorator
#     @__say_decorator_generator("减")
#     def minus(self,n):
#         self.__result -= n
        
#     @__check_num_decorator
#     @__say_decorator_generator("乘以")
#     def multiply(self,n):
#         self.__result *= n
        
#     @__check_num_decorator
#     @__say_decorator_generator('除以')
#     def division(self,n):
#         self.__result /= n
    
    
#     def show(self):
#         self.__say_word("等于",self.__result)
        
        
# c1 = Calculator(2)
# c1.add(6)
# c1.minus(4)
# c1.multiply(5)
# c1.show()


#代码11 
import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak('我的名字是蔡启越')

class Calculator(object):
    """
    装饰器，只能接受 func 被装饰函数，因为这是 系统自动的  add = __say_decorator(add)
    装饰器内部的 inner 函数的参数 必须和 被装饰函数 的 形参 一致
    所以 装饰器 和 闭包 inner 的 形参 都固定或者说 受到限制，不灵活
    
    """

    
    
    def __say_decorator_generator(say_word=""):
        """
        这就是装饰器生成器
        内部是一个装饰器，return 该装饰器
        
            say_decorator = __say_decorator_generator(say_word) 装饰器生成器，返回一个 装饰器
            通过 不同的 say_word 创建了 不同的适合各个函数 的装饰器
    
      @__say_decorator_generator(say_word) 本质上是一个装饰器
       def ....
        """
        def __say_decorator(func):
            def inner(self,n):
                self.__say_word(say_word,n)# 把语音播报的实现过程 封装起来，需要改动该语音实现过程的话，只需要改一个地方
                return func(self,n)
            return inner
        return __say_decorator
    
    #装饰器
    def __check_num_decorator(func):#传入 需要被装饰 的函数
        def inner(self,n):#内部实现 闭包
            if not isinstance(n,int):#需要新加的逻辑流程
                raise TypeError("not int")
            return func(self,n)#返回，并执行原来的函数
        return inner#返回闭包
    
    @__check_num_decorator
    @__say_decorator_generator()
    def __init__(self,n) -> None:
        self.__result = n
        
    def __say_word(self,say_word,n):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(say_word + str(n))
    
    @__check_num_decorator
    @__say_decorator_generator('加')
    def add(self,n):
        self.__result += n
        return self
        
    @__check_num_decorator
    @__say_decorator_generator("减")
    def minus(self,n):
        self.__result -= n
        return self
        
        
        
    @__check_num_decorator
    @__say_decorator_generator("乘以")
    def multiply(self,n):
        self.__result *= n
        return self
        
    @__check_num_decorator
    @__say_decorator_generator('除以')
    def division(self,n):
        self.__result /= n
        return self#实例方法，返回实例本身，可以 进行 链式调用
    
    def clear(self):
        self.__result = 0
        self.__say_word('结果清零，当前值为',0)
        return self
    
    @property
    def result(self):
        return self.__result
    
    
    def show(self):
        self.__say_word("等于",self.__result)
        return self
        
        
c1 = Calculator(2)
c1.add(4).add(10).multiply(10).division(2).show().clear()#链式调用

print(c1.result)