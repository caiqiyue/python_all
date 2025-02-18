from py2neo import *

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()
alice = Node('Person',name = 'alice',age = 10)
bob = Node('Person',name = 'bob',age = 20)
caral = Node('Person',name = 'caral',age = 20)

g.create(alice)
g.create(bob)
g.create(caral)


cursor = g.run('match (p:Person) return p')


print(cursor.plan())#还不清楚，但是估计没啥用
print(cursor.preview())

"""
表格形式预览cursor中的数据
----------------------------------------
 (_142:Person {age: 10, name: 'alice'})
 (_143:Person {age: 20, name: 'bob'})
 (_144:Person {age: 20, name: 'caral'})
"""

print(cursor.keys())#['p'],cursor内部是 列表包着字典，返回字典的键

for record in cursor:#说明cursor中一定至少实现了 getitem  或者 next
    print(type(record))#<class 'py2neo.cypher.Record'>


while cursor.forward():# cursor中 有三条记录  cursor指向最低下一个，然后forward按照指定步长往上走 cursor。forward返回还能走的长度
    print(cursor.current)#cursor.current表示，当前指向的那条记录,并不一定是 Node类型
    
    
    
    
    
