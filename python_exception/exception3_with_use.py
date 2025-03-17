

class Text():
    """
    with  text() as e:
       body
    执行的流程就是
    上下文表达式  text()调用 __enter__方法，返回对象 给 e
    执行 with语句体，如果出现异常，将异常跟踪信息返回给 __exit__方法，
    exit方法中，自定义对异常处理的逻辑 ，如果决定向外界抛出异常终止程序，那么就返回 True，反之返回false   
    """
    def __enter__(self):
        print("enter")
        return self
        
        
    def __exit__(self,exc_type,exc_val,exc_tb):
        # exc_type 代表异常的类型  exc_val 代表 异常值   exc_tb 异常的追踪信息
        """
        在with语句体中的代码执行如果出现异常，那么异常信息就会返回给 __exit__，exit就会返回异常信息，
        但是 如果 exit 返回 True那么就不会抛出异常，如果是False就会将异常信息抛出
        """
        print(self,exc_type,exc_val,exc_tb)
        import traceback
        #打印异常的追踪信息
        print(traceback.extract_tb(exc_tb))#[<FrameSummary file c:\Users\ASUS\PycharmProjects\python_all\python_exception\exception3_with_use.py, line 24 in <module>>]
        print("exit")
        return True
        
        
        
with Text() as x:
    1 / 0
    print("body",x)
    
"""
Text()是上下文表达式，里面实现了 __enter __exit__ 方法
with语句 使用时，就会线 __enter__ ----> body ---->  __exit__

as x  x应该是 上下文管理器 __enter__的返回值

enter
body
<__main__.Text object at 0x0000028D662C5040> None None None
exit

"""