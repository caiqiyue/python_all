



class Text():
    def t(self):
        print('ttttt')
        
    def close(self):
        print("资源释放")
        
        
    def __enter__(self):
        """
        返回的 是 Text()的实力对象
        """
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.close()
        
        
with Text() as t:
    t.t()
    

class Text2():
    """
    必须实现 close实例方法，才能被 contextlib作为装饰器
    """
    def t2(self):
        print('ttttt')
        
    def close(self):
        print("资源释放")
    
import contextlib

with contextlib.closing(Text2()) as t2:
    t2.t2()
