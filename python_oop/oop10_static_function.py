class Person:
    @staticmethod
    def run():
        print("这是一个静态方法")
        

#静态方法中，类，实例都可以调用，就是个普通函数

p = Person()

p.run()

Person.run()

func = Person.run

func()