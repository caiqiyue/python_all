from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob',age = 20)
caral = Node('Person',name = 'caral',age = 20)

g.create(alice)
g.create(bob)
g.create(caral)


# print(type(g.run('match (p:Person) return p')))#<class 'py2neo.cypher.Cursor'>

cursor1 = g.run('match (p:Person) return p.name,p.age')#执行cypher语句后，返回一个 cursor对象

print(type(cursor1.to_data_frame()))#将查询的结果，转成 dataframe 结构
#此外，to_matrix,to_subgraph,to_table,to_series,to_ndarray，可以将查询结果转化成这些结果，但是 应该是 pd np更常用

print(cursor1.summary())#打印所有结果和状态


print(cursor1.data())
# [{'p': Node('Person', age=10, name='alice')}, {'p': Node('Person', name='bob')}, {'p': Node('Person', name='caral')}]
# 以列表包字典的形式 返回 所有节点 






cursor2 = g.run('match (p) where p.name = $x return p.age, p.name',x = 'alice')


print(cursor2.evaluate(1))#返回 如果 cypher语句返回的是  字段值 ，则 evaluate返回第一个字段的值（默认0），如果为1，就是第二个字段的值


print(g.run("CREATE (a:Person) SET a.name = 'Alice'").stats())#打印执行该cypher语句的结果
"""
{'contains_updates': True, 'nodes_created': 1, 'nodes_deleted': 0, 'properties_set': 1, 'relationships_created': 0, 'relationships_deleted': 0, 'labels_added': 1, 'labels_removed': 0, 'indexes_added': 0, 'indexes_removed': 0, 'constraints_added': 0, 'constraints_removed': 0, 'contains_system_updates': False, 'system_updates': 0}
"""

