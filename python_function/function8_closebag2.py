

def outer():
    
    num = 10
    num1 = 11
    def inner():
        """
        如果闭包内，想要修改闭包外的 变量 ，如果不加 nonlocal，那么就是在闭包内新增变量，不影响外部变量
        如果 加了 nonlcoal，那么闭包内修改的就是外部变量了
        """
        num = 100
        nonlocal num1
        num1 = 101
        print("num",num)
        print("num1",num1)
        

    print("beofre inner num",num)
    print("before inner num1",num1)
    inner()
    print("after inner num",num)
    print("after inner num1",num1)    
    
    
      
    return inner

outer()