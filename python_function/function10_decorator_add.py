






def printLine(func):
    def inner():
        print("---------------------")
        func()
        
    return inner

def printStar(func):
    def inner():
        print("***************")
        func()
    return inner

@printLine #  等同于  test = printLine(test)
@printStar # 等同于 test = printStar(test)
def test():
    """
    多个装饰器修饰一个函数时，从上到下的装饰，从下到上的执行
    """
    print("test")
    
test()