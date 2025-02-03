from py2neo import *


a = Node('Person',name='caiqiyue')
b = Node("Person",name = 'xxxx')

#创建  关系节点的  方式 1
r = Relationship(a,'Knows',b,name = 'relation',date = '2020/10/1')

#创建  关系节点  的 方式 2
WORK = Relationship.type('Work')
r2 = WORK(a,b)


#和关系本身相关的方法
print(type(r))#<class 'py2neo.data.Knos'>

print(type(r).__name__)#Knows

print(r.nodes)#(Node('Person', name='caiqiyue'), Node('Person', name='xxxx'))

print(r.start_node)#(:Person {name: 'caiqiyue'})

print(r.end_node)#(:Person {name: 'xxxx'})

#和关系 的属性 相关的方法
print("=================================================================================")
print(r['name'])#打印关系的 属性值
print(r['date'])

print(len(r))#返回 关系节点 有多少个属性

print(dict(r))#以键值对的形式 返回 关系节点的属性值

print(r.get('name'))#使用 get 函数 返回 关系节点的 属性值 


print(r.items())#字典形式的三件套

print(r.keys())

print(r.values())

r.setdefault('age',default=20) #如果 有这个 属性 就返回 ，没有 就根据 默认值 设置该属性
print(r['age'])

r.update({'name':'hahahahah'}) #根据 字典 更新 属性值
print(r['name'])

del r['date'] #删除  单个 属性
print(dict(r))

r.clear()#清楚 所有 关系节点的  属性
print(dict(r))