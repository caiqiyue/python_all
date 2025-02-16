class Person:
    pass


p = Person()

# p.age = 18
# p.sex = 'male'
# print(p.age,p.sex)

# #__dict__中包含此对象拥有的所有属性
# print(p.__dict__)

# #p.age是p中的一个变量，指向内存某一位置，存放数值18的位置
# print(id(p))#2393710559632
# print(id(p.age))#2393705704272


#===============================================================
# p.pets = ['小黑','小黄']
# print(p.pets,id(p.pets))#1751107854784

# p.pets.append('小兰')#注意，这是访问操作，先是取出p.pets，然后再是在取出来的列表中添加元素
# print(p.pets,id(p.pets))#1751107854784

# p.pets = [1,2,3]#这是修改操作，直接对着p.pets修改
# print(p.pets,id(p.pets))#1751110926016


# p.height = 180
# print(p.height)
# del p.height

# print(p.height)#注意，删除的是对数值180的引用，也就是对象p中存放数值180内存地址的p.height,若垃圾回收机制发现没有任何东西引用180时，就会回收它

#=============================================================

p1 = Person()
p2 = Person()

p1.age = 90
p2.age = 90


#虽然是不同的对象，但是属性的id却是相同，证明了，p1.age和p2.age是引用的数值90的内存地址
print(id(p1.age))#2187342926992
print(id(p2.age))#2187342926992
p1.age = 89
print(id(p1.age))#1740685005936,修改为89,并不是在90的基础上减一，而是新找一个89，保存数值89的内存地址
print(id(p2.age))


#可发现，换成可变类型，列表，数据一样，但是内存地址就不一样了，因为怕修改了p1的，影响到p2
p1.pets  = [1,2]
p2.pets = [1,2]
print(id(p1.pets))#2159694799296
print(id(p2.pets))#2159697870336