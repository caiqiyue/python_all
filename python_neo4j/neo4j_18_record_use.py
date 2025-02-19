from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob',age = 20)
caral = Node('Person',name = 'caral',age = 20)

alice_bob = Relationship(alice,'KNOWS',bob)

bob_caral = Relationship(bob,'KNOWS',caral)

caral_alice = Relationship(caral,'KNOWSA',alice)


g.create(alice)
g.create(bob)
g.create(caral)

g.create(alice_bob)
g.create(bob_caral)
g.create(caral_alice)




cursor1 = g.run('match (p1:Person)-[r:KNOWS]->(p2:Person) return p1,p2,r')


record = next(cursor1)



cursor = g.run('match (p:Person) return p.name,p.age')

record1 = next(cursor)
# print(next(cursor))


# record1 = next(cursor)
print(record1[1])#record对象，record[0]，返回该对象中Node节点的第一个属性值，1就是第二个属性值
print(record1['p.name'])#如果要以  key 来 获取属性值的话  ，要看cypher语句返回的名称，而非字段名本身



print(len(record1))#返回该节点 所包含的 属性个数
print(dict(record1))#以字典的形式 返回

print(record1.data())#以字典的形式，返回所有属性值

print(record1.get("p.name"))#get获取属性值

print(record1.index('p.age'))#获取  是第几个属性

print(record1.items())#[('p.name', 'alice'), ('p.age', 10)]

print(record1.keys())#['p.name', 'p.age']

print(record1.values())#['alice', 10]

graph = record.to_subgraph()
"""
对于，转化成子图，需要看cypher语句返回的是什么数据
return p.age,p.name 这样就 转换不成 子图

return p1,p2,r  就可以生成子图
"""

print(type(graph))#<class 'py2neo.data.Subgraph'>