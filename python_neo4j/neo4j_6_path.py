from py2neo import *
alice, bob, carol = Node(name="Alice"), Node(name="Bob"), Node(name="Carol")
abc = Path(alice, "KNOWS", bob, Relationship(carol, "KNOWS", bob), carol)
"""
这行代码创建了一个路径（Path）对象 abc，该路径由以下几部分组成：

Alice 与 Bob 之间有一条 "KNOWS" 关系。
Carol 与 Bob 之间也有一条 "KNOWS" 关系，使用了 Relationship 来表示。
Carol 是路径的终点。
Path 对象是一个图的子结构，可以包含节点和它们之间的关系。
"""

print(abc.graph)#图

print(abc.nodes)#(Node(name='Alice'), Node(name='Bob'), Node(name='Carol'))

print(abc.start_node)#({name: 'Alice'})

print(abc.end_node)#({name: 'Carol'})

print(abc.relationships)#(KNOWS(Node(name='Alice'), Node(name='Bob')), KNOWS(Node(name='Carol'), Node(name='Bob')))

#返回集合，每个集合 都包含 一类关系类型的关系节点 eg: （全是 以 knows为关系的关系节点），（全是 以 work为关系的关系节点）
print(abc.types())#(KNOWS(Node(name='Alice'), Node(name='Bob')), KNOWS(Node(name='Carol'), Node(name='Bob'))) frozenset({'KNOWS'})

#遍历  路径节点中的 所有 元素 包含 实体节点 关系节点
for item in walk(abc):
    print(item)
    
"""
({name: 'Alice'})
(Alice)-[:KNOWS {}]->(Bob)
({name: 'Bob'})
(Carol)-[:KNOWS {}]->(Bob)
({name: 'Carol'})
"""