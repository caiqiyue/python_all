
"""
函数的参数传递，有两种形式
1.值传递
比如说，a = 10 ,变量a保存了   内存中int类的实例对象10的  内存地址
当a作为实参，传递到函数的形参num中时，num会将 内存中的10，复制一份，并在内存中开辟一块新的内存区域存储int类的新实例对象10，
并且num保存这个新实例对象的内存地址。也就是说，传递的是10这个值，而非内存地址

2.引用传递（地址传递）
同样，当a作为实参，传递给函数的形参num中时，num会直接指向 内存中的10，也就是说a和num保存着同样的内存地址
那么函数内部对num的修改，也会影响到a，说明传递的是内存地址

但是python与众不同，它只遵循引用传递，但是对于可变数据类型和不可变数据类型的引用传递又不太一样
对于可变数据类型 函数的实参和形参都会指向同一个内存地址，函数内部对其修改，外部的实参也会收到影响
对于不可变数据类型，  一开始 实参和形参都会指向同一个内存地址，但是 当函数内部修改不可变数据类型时，
python会复制一份这个不可变数据类型的值，然后存储到另一个新的内存空间中，且将新的内存地址赋值给形参，实参不变
"""


can_change_data = [1,2,3]#可变数据类型

can_not_change_data = 10#不可变数据类型


def func(can,notcan):
    print(can,id(can))#1919111291328，形参和实参（列表）的内存地址一样，说明这是引用传递，传递的是内存地址
    
    can.append(100)#可变数据类型，变化
    
    print(can,id(can))#1919111291328  内存地址不变  引用传递
    
    
    print(notcan,id(notcan))#1919105854032  此时的  形参和实参（整型10）内存地址一样
    
    notcan = 19 #修改形参
    
    print(id(notcan))#1919105854320  形参的内存地址变化
    
    
print(can_change_data,id(can_change_data))#1919111291328  列表的内存地址
print(can_not_change_data,id(can_not_change_data))#1919105854032  10  的 内存地址


func(can_change_data,can_not_change_data)

print(can_not_change_data,id(can_not_change_data))#1919105854032  数值没有变，说明函数内部对  不可变数据类型的修改  不影响外部
print(can_change_data,id(can_change_data))#1919111291328 数据变了