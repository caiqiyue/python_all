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

rs = RelationshipMatch(graph=g,nodes=None, r_type='KNOWS', predicates=(), order_by=(), skip=None, limit=None)
"""
nodes 头结点，尾节点 可以传递 列表和 元组
r_type就是 关系 类型
predicates 谓语动词，传递 cypher语句那种
skip跳过开头几个
limit省略 结尾几个
order_by 排序
"""
for relation in iter(rs):
    print(relation)
    
print(rs.all())#以列表形式返回所有符合的关系节点

print(rs.count())#返回结果个数

print(rs.exists())#返回是否 有 结果

print(rs.first())#返回 结果中的第一个 关系节点

#一下这些 约束 可以在 relationshipmatch的时候 加进去，也可以 在返回的结果中 进一步 进行 筛选

rs.limit(1)

rs.skip(1)

for item in rs.where("_.date = '2020'"):
    print(item)


for item in rs.order_by('_.date'):#按照 date属性排序
    print(item)

