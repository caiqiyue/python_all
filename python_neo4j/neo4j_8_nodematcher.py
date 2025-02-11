from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob')
caral = Node('Person',name = 'caral')

g.create(alice)
g.create(bob)
g.create(caral)

"""
很明显，matcher匹配器，必须基于图

这是 NodeMatcher中的  __iter__方法
    def __iter__(self):
        for node in self.match():
            yield node.identity
"""
#nodematcher的用法

node_matcher = NodeMatcher(g)
result = node_matcher.match('Person',name='alice',age = 10)#后面也可以跟 where条件语句

print(result)#<py2neo.matching.NodeMatch object at 0x0000025B8B597FA0>

node_iterator = iter(node_matcher)#调用 内部的 __iter__方法，返回 节点的 id值
for node in node_iterator:
    print(node)

print(len(node_matcher))#返回 匹配中的 结果 个数

print(0 in node_matcher)#判断 节点id 是否 在 匹配器中

print(node_matcher[24])#返回 id值=24 的 节点实例 (_24:Person {age: 10, name: 'alice'}),，没有则报错

print(node_matcher.get(25))#返回 id值=25 节点实例 (_25:Person {name: 'bob'})，没有则报错