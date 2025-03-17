


class MyException(BaseException):
    """
    自定义异常必须继承自 BaseException
    """
    def __init__(self,err_msg,err_code):
        self.em = err_msg
        self.ec = err_code
        
    def __str__(self):
        """
        对实例对象的描述
        """
        return self.em + str(self.ec)
    
    

def getAge(age):
    if age < 0:
        raise MyException("年龄不能为负数",404)#手动抛出异常
    else:
        print("年龄设置成功")
        
        
try:
    getAge(-1)
except MyException as e:#e 是 MyException 实例对象 print(e) 调用 内部的__str__函数
    print(e)
    
