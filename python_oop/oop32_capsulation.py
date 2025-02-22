from oop31_practice import Calculator

#将 计算机 这个类 封装好 外部 直接引入该包 随意调用，只需要把它当做内部工具使用，外部不需要关心它的内部细节
c = Calculator(2)
c.add(1).show()