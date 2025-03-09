

"""
假设一个函数中，有四个参数，但是参数d在某一时间段内，几乎都等于1，不怎么变，可以设置为 缺省参数  但是 万一以后变了，
就要修改缺省参数，那么之前使用d=1的函数就会有问题
"""
def test(a,b,c,d=1):
    print(a + b + c + d)
    

#偏函数的第一种实现方式
def test2(a,b,c=5):
    test(a,b,c)
    
test2(1,2)

#第二种方式
import functools

new_func = functools.partial(test,c=3)#前面是 函数 ，后面是 你偏爱的 参数，然后会返回一个新的函数
print(new_func,type(new_func))

new_func(1,2)

#使用场景

c = '100010'
rs = int(c,base=2)#将字符串，以二进制的方式转乘整数
print(rs)
str2int_binary = functools.partial(int,base=2)
out = str2int_binary(c)
print(out)