



import contextlib


@contextlib.contextmanager
def test():
    """
    被装饰之后，
    yield 之前的 作为 __enter__
    yield 之后的 作为 __exit__
    yield 返回的值 作为 __enter__的返回值
    """
    print(1)
    yield 'www'
    
    print(2)
    
# with test() as w:
#     print(3,w)
    
    

@contextlib.contextmanager
def zero_exception():
    """
    先执行 try语句，
    再执行 except语句
    """
    try:
        yield
    except ZeroDivisionError as e:
        print('自定义异常：',e)


#现在相当于 1/0 是 功能代码，而 zero_exception()  是我们的 异常检测代码，所以 功能代码 和 异常检测 代码 分离了
with zero_exception():
    1 / 0