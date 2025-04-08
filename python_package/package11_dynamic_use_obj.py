

class MyClass(object):
    def my_method(self):
        print("this is my self-defined method")
        
        

obj = MyClass()

method_name = 'my_method'

#动态获取 该属性的 函数对象
func = getattr(obj,method_name)


#先用字符串表达出 属性的函数调用  obj.my_method(),然后用 exec将字符串转为python语言执行

func_exe = f"obj.{method_name}()"
exec(func_exe)
#执行函数
func()