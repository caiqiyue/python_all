

def fashuoshuo():
    print("fashuoshuo")
    
def fatupian():
    print("fatupian")
    


"""
功能代码要和业务逻辑代码分开
"""
boundindex = 1
if boundindex == 1:
    print('登录验证')#在业务逻辑代码中加入 登录代码，复用性太差，代码冗余
    fashuoshuo()
else:
    fatupian()