from py2neo import *
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob')
caral = Node('Person',name = 'caral')

alice_bob = Relationship(alice,'Knows',bob)
bob_caral = Relationship(bob,'Konws',caral)


dive = Node('Person',name = 'dive')
candy = Node('Person',name = 'candy')
cacy = Node('Person',name = 'cacy')

dive_candy = Relationship(dive,'Knows',candy,date = 100)
candy_cacy = Relationship(candy,'Konws',cacy)


#子图2
g2 = Subgraph([dive,candy,cacy],[dive_candy,candy_cacy])

#子图1
g1 = Subgraph([alice,bob,caral],[alice_bob,bob_caral])

# print(g1 | g2)#返回两个子图的 并集

# print(g1 & g2)#返回两个子图的 交集

# print(g1 - g2)#返回两个子图的 差集

# print(g1 ^ g2)#返回 对称差集

print(g1.keys())#frozenset({'name', 'age'}) 返回所有的  子图中 实体节点的  属性名称（不包含 关系节点的 属性值）

print(g1.relationships)#<interchange.collections.SetView object at 0x0000018ABBF06970>  返回 所有 关系节点

print(g1.labels())#frozenset({'Person'})  返回 所有 标签

print(g1.nodes)#返回所有  节点  <interchange.collections.SetView object at 0x0000029825E16CD0>

print(g1.types())#frozenset({'Konws', 'Knows'})  返回 所有  关系节点  的  关系类型 

for node in g1.nodes:
    print(node)
    
"""
(:Person {age: 10, name: 'alice'})
(:Person {name: 'bob'})
(:Person {name: 'caral'})

也就是 子图的 nodes 和  relationships 返回一个 可迭代对象
"""