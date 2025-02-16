from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10,birth=2020)
bob = Node('Person',name = 'bob',age=19,birth = 2018)
caral = Node('Person',name = 'caral',age = 20,birth = 2015)
aday = Node('Person',name = 'aday',age = 20,birth = 2010)
boody = Node('Person',name = 'boody',age = 10,birth = 2015)
candy = Node('Person',name = 'candy',age = 20,birth = 2021)
name_null = Node('Person',age = 10,birth = 2021)

g.create(alice)
g.create(bob)
g.create(caral)
g.create(aday)
g.create(boody)
g.create(candy)
g.create(name_null)


nodes = NodeMatcher(g)

print(nodes.match('Person',name=IS_NOT_NULL()).all())#IS_NOT_NULL 只要name属性不为空就满足条件

print(nodes.match('Person',name=IS_NULL()).all())#name is null

print(nodes.match(age = EQ(10)).all())# age == 10

print(nodes.match(age = GE(10)).all())#age >= 10

print(nodes.match(age = LE(20)).all())# age <= 20

print(nodes.match(age = GT(10)).first()) # age >10

print(nodes.match(age = LT(20)).first())#age < 20

print(nodes.match(name = Contains('a')).first()) #name 包含 ‘a’

print(nodes.match(name = STARTS_WITH('a')).first())#name 以 a 开头

print(nodes.match(name = EndsWith('b')).first())#name 以 b结尾

print(nodes.match(name = LIKE('a.*e')).first())#like 里面可以使用正则表达式

print(nodes.match(name = IN(['alice','bob'])).all())#name 要么是 alice 要么是 bob

print(nodes.match(age = AND(GE(10),LE(20))).all())#age >= 10 <= 20

print(nodes.match(age = OR(GE(10),LE(20))).all())#age >= 10 或者 <=20

print(nodes.match(name = XOR(STARTS_WITH('a'),ENDS_WITH('b'))).all())#name 要么 以a开头，要么以b结尾，不能同时  xor是异或操作

print(nodes.match('Person').where("_.age % 10 = 0").first())# age 对10 取余 余数为0