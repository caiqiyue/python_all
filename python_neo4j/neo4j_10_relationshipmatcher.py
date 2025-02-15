from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob')
caral = Node('Person',name = 'caral')

alice_bob = Relationship(alice,'KNOWS',bob,date='2020')
alice_caral = Relationship(alice,'KNOWS',caral,date='2029')
bob_caral = Relationship(bob,'LIKES',caral,date='2019')
caral_alice = Relationship(caral,'MATES',alice,date='2009')

g.create(alice)
g.create(bob)
g.create(caral)
g.create(alice_bob)
g.create(bob_caral)
g.create(caral_alice)
g.create(alice_caral)

relation_matcher = RelationshipMatcher(g)#和 NodeMatcher一样，只需要传递 图 即可

matcher_iterator = iter(relation_matcher)#iter（）调用 类内部的 __iter__，返回的节点 id
for i in matcher_iterator:
    print(i)

print(len(relation_matcher))#返回 结果 个数

print(3 in relation_matcher)#判断 该 节点id值是否在 匹配到 的结果中 True

print(relation_matcher[3])#返回 结果中的  该 id值 的节点，没有则报错  (alice)-[:KNOWS {date: '2020'}]->(bob)

print(relation_matcher.get(3))#返回节点id=3的节点，没有则报错  (alice)-[:KNOWS {date: '2020'}]->(bob)

rs = relation_matcher.match(r_type='KNOWS')#返回的是  relationshipmatch对象，注意这是 relationshipMatcher 匹配器
"""
match(nodes = ,r_type=  节点属性=)

nodes,要求 输入的是  元组或者序列（列表也行），里面可以是 开始节点 也可以是 结束节点 如果不输入，就是任意节点
r_type 是 关系 的 类型
后面可以 输入 关系 的 属性

返回的是 relationshipmatch 对象 可以 first  where  iter
"""

print(rs.first())#(alice)-[:KNOWS {date: '2020'}]->(bob)
for relation in iter(rs):#返回所有 匹配到的  关系节点
    print(relation)#(alice)-[:KNOWS {date: '2020'}]->(bob)  (alice)-[:KNOWS {date: '2029'}]->(caral)


