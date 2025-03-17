




def decorator(func):
    def inner(*args,**kwargs):
        print("****************")
        print(args,kwargs)#现在的args和kwargs是元组和字典，并不是我们要的参数，需要解包
        func(*args,**kwargs)
    return inner




@decorator
def printNum(num1,num2,num3):
    print(num1,num2,num3)
    
    
@decorator
def printNum2(num):
    print(num)
    
    
printNum(1,2,num3=3)
printNum2(10)