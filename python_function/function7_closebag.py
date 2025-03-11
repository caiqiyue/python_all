


def test():
    """
    内部函数test2，使用外部变量 a，同时，外部函数test，把内部函数test2返回，那么a + test2 被称为闭包
    """
    a = 10
    def test2():
        print(a)
        
    return test2

newFunc = test()
newFunc()



def line_config(content,lenght):
    """
    比如说，我想画一条带有文字的线，如果不是用闭包，每次都要
    line('xx',20)
    line('xxxxx',10)
    这时候不太方便
    """
    def line_draw():
        print("-"*(lenght // 2) + content + "-"*(lenght // 2))
    return line_draw

line1 = line_config('nihao',10)

line2 = line_config('hahaha',4)

line1()

line1()

line2()

