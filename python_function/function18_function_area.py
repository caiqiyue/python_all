





print("zzz")# B : 内建模块 作用域 适用于 所有模块（.py文件）

num = 10#G 全局作用域  作用于当前 模块

def test():
    num = 10#内函数外部，外函数内部的 作用域
    def test2():
        num = 10 #L：函数内部作用域
        print(num)


#python中没有块级代码作用域，比如 if for  while 这种代码块
for i in range(10):
    print(i)#块级代码
    
    
print(i)#但是在块级代码外部，也能访问