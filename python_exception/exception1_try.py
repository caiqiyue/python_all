

try:
    1 / 0
    print(name)
    
except (ZeroDivisionError,NameError):
    print("两种异常组合")   
    
except ZeroDivisionError:
    print("除0异常")
except NameError as ne:
    print("变量名异常",ne)
    
else:
    print("没有异常")
    
finally:
    print("都会走这一步")