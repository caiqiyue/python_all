

from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob',age = 2)
caral = Node('Person',name = 'caral',age = 12)
g.create(alice)
g.create(bob)
g.create(caral)

"""
NodeMatch(graph, labels=frozenset({}), predicates=(), order_by=(), skip=None, limit=None)
labels要传入 [label1,label2]，它会被转为 不可修改的元组 
predicates 表示 传入 谓词  比如  a in [a,b,c]
skip 表示 跳过 返回的结果 的前几条
limit 限制返回的 数量
order_by 排序
"""
#NodeMatch(graph=g,labels=['Person']).where("_.name = 'alice' and _.age = 10 ")
result = NodeMatch(graph=g,labels=['Person']).order_by('_.age')#NodeMatch 没有 __call__函数，直接匹配节点而且 标签 要通过 列表传入，其他传递方式都不行

print(result)#<py2neo.matching.NodeMatch object at 0x000001B614D994F0>


print(len(result))#返回匹配中的结果个数

node_iterator = iter(result)#代用 内部__iter__返回的是节点，而不是id
for node in node_iterator:
    print(node)
    
print(result.all())#[Node('Person', age=10, name='alice'), Node('Person', name='bob'), Node('Person', name='caral')],列表形式返回所有匹配到的节点

print(result.count())#饭弧节点个数

print(result.exists())#是否 匹配中结果

print(result.first())#返回匹配中的第一个结果

print(result.limit(2))#限制返回结果的个数


