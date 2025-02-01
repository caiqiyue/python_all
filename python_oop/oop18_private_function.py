class Person:
    __age =  10
    
    def __run(self):
        #私有化方法，名称 变成了 _Person__run 
        print("run")
        
    def _Person__run(self):
        #如果这么写的话，就会把上面的  私有化方法 run 给覆盖
        print("xxxx")
        

p = Person()
print(Person.__dict__)#{'__module__': '__main__', '_Person__age': 10, '_Person__run': <function Person.__run at 0x0000028BDFA913A0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
#print(p.__run())
#同理，私有属性和私有方法一样，都是伪私有，在dict中被编译器更换了名称 存储着