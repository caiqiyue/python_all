



#整除和余数的应用场景
#可以代表 行 和 列
num = 10
#假设行和列都从0开始
row = num // 4
col = num % 4


# is 比较 的是 唯一标识 ，==  比较的内容
"""
python中万物皆对象， num = 10 ,就是 在内存中 创建一个 int类的 实例对象 10，并分配内存给它，同时将 唯一标识 返回给 引用这个 10 的变量
"""
a = [1]
b = [1]
print(a == b)#True
print(a is b)#False，这涉及 列表的 内存 

#链式比较
print(1 < 2 <10)



print(bool(1))
print(bool(0))


"""
or 和 and 就是识别到哪一个表达式，就把哪一个表达式 返回
因为 当python解释器 看到 or 的左边是 1 非零即真，则整个 or 的表达结果肯定为真，就不会再看or右边的式子，直接输出了 or左边的式子，而此时的式子是 1，所以输出了1
当python解释器 看到 and 的左边 是0 ，代表False，则整个 and 表达式结果肯定为假，就不会再看 and 右边的式子，直接输出了 and 左边的式子 0
当python解释器看到 and 的左边是 1，代表True，那么还需要继续往后看，and 的右边 是3也是 True，那么整个and 的结果是True，此时识别到右边的式子，则返回右边式子
当python解释器看到 or左边的是 1，代表True，不需要再看 or右边的式子了，此时识别到 or左边的式子，直接返回or左边的式子
当python解释器看到 or左边的是 0 代表False，还需要再看 右边的式子，右边的式子是False，所以or表达式的结果为False，此时识别到右边，返回右边的式子False
第二个or 的左边结果 是 False，则还需要看 第二个 or 右边的式子，右边式子是 6，则整个or表达式结果式True，此时看到 第二个or的右边式子，返回该式子
"""
print(1 or False) # 结果 是 1 而不是 True
print(0 and True) # 结果 是 0 而不是 False
print(1 and 3)#结果 是 3
print(1 or 3)#结果 是 1
print(0 or False)
print(0 or False or 6)# 6 