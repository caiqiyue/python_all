class Person:
    @classmethod
    def eat(cls,q):
        print("eat",cls,q)
        
p = Person()

#类方法的话，类可以调用，实例也可以调用，第一个参数 最好是类本身；使用实例，调用类方法的时候，传递的还是类本身，而非实例
Person.eat('231')
p.eat('3234')


#我们当然也可以像取出实例方法中的函数一样，取出类方法中的函数
#但是不一样的是，取出实例方法中的函数，可以给self形参手动传递，而且不一定得传实例本身
#但是，取出类方法中的函数，它还是会自动给cls形参传递类本身，这是因为classmethod装饰器起到的作用
func = Person.eat
func('asa')


class Student(Person):
    pass

Student.eat('这是子类，传给cls子类')#eat <class '__main__.Student'> 这是子类，传给cls子类