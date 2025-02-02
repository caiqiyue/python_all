#pip install py2neo -i https://pypi.tuna.tsinghua.edu.cn/simple
from py2neo import Node, Relationship
from py2neo import Graph, Subgraph

test_graph=Graph("http://localhost:7474", auth=("neo4j", "wangmeng"))
test_graph.delete_all()#删除所有已有节点
#
# # 定义node
node_1 = Node('英雄',name = '张无忌')
node_2 = Node('英雄',name = '杨逍',武力值='100')
node_3 = Node('派别',name = '明教')
# 存入图数据库
test_graph.create(node_1)
test_graph.create(node_2)
test_graph.create(node_3)

node_1_to_node_2 = Relationship(node_1,'教主',node_2)
node_3_to_node_1 = Relationship(node_1,'统领',node_3)
node_2_to_node_2 = Relationship(node_2,'师出',node_3)

test_graph.create(node_1_to_node_2)
test_graph.create(node_3_to_node_1)
test_graph.create(node_2_to_node_2)

from py2neo import Path
# 建一个路径：比如按照该路径查询，或者遍历的结果保存为路径
node_4,node_5,node_6 = Node(name='阿大'),Node(name='阿二'),Node(name='阿三')
path_1 = Path(node_4,'小弟',node_5,Relationship(node_6, "小弟", node_5),node_6)
test_graph.create(path_1)
print(path_1)

# 创建一个子图，并通过子图的方式更新数据库
node_7 = Node('英雄',name = '张翠山')
node_8 = Node('英雄',name = '殷素素')
node_9 = Node('英雄',name = '狮王')

relationship7 = Relationship(node_1,'生父',node_7)
relationship8 = Relationship(node_1,'生母',node_8)
relationship9 = Relationship(node_1,'义父',node_9)
subgraph_1 = Subgraph(nodes =[node_7,node_8,node_9],relationships = [relationship7,relationship8,relationship9])
test_graph.create(subgraph_1)

# 创建一个新的事务
transaction_1 = test_graph.begin()

# 创建一个新node
node_10 = Node('武当',name = '张三丰')
transaction_1.create(node_10)
# 创建两个关系：张无忌→（师公）→张三丰   张翠山→（妻子）→殷素素
relationship_10 = Relationship(node_1,'师公',node_10)
relationship_11 = Relationship(node_7,'妻子',node_8)

transaction_1.create(relationship_10)
transaction_1.create(relationship_11)

transaction_1.commit()

node_x = Node('英雄',name ='韦一笑')
test_graph.create(node_x)
test_graph.run('match (n:英雄{name:\'韦一笑\'}) delete n')

# 删除一个节点及与之相连的关系
test_graph.run('match (n:英雄{name:\'韦一笑\'}) detach delete n')
# 删除某一类型的关系
test_graph.run('match ()-[r:喜欢]->() delete r;')

# 删除子图
# delete(self, subgraph)

# 改
# 改的基础也是查询，查到就可以改，因此本文的重点放在查询上，下面示例简单修改。

# 改
# 将狮王的武力值改为100
node_9['武力值']=100
# 本地修改完，要push到服务器上哦
test_graph.push(node_9)

# 查
# 最重要的环节到了，一般来说，我们主要是查询，按照路径等、所有节点、关系等，我自己的学习需求还包括了一些统计特性的计算。主要使用下面的方式。
# 为了使用更复杂查询，将图数据库扩充如下：

# 为了便于查询更多类容，新增一些关系和节点
transaction_2 = test_graph.begin()

node_100 = Node('巾帼',name ='赵敏')
re_100 = Relationship(node_1,'Love',node_100)

node_101 = Node('巾帼',name ='周芷若')
re_101 = Relationship(node_1,'knows',node_101)
re_101_ = Relationship(node_101,'hate',node_100)


node_102 = Node('巾帼',name ='小昭')
re_102 = Relationship(node_1,'konws',node_102)

node_103 = Node('巾帼',name ='蛛儿')
re_103 = Relationship(node_103,'Love',node_1)

transaction_2.create(node_100)
transaction_2.create(re_100)
transaction_2.create(node_101)
transaction_2.create(re_101)
transaction_2.create(re_101_)
transaction_2.create(node_102)
transaction_2.create(re_102)
transaction_2.create(node_103)
transaction_2.create(re_103)
test_graph.commit(transaction_2)#新版本要求这个
# transaction_2.commit()

from py2neo import NodeMatcher
# 定义查询
nodes = NodeMatcher(test_graph)

# 单个节点，按照label和name查询
## 查询节点：杨逍
node_single = nodes.match("英雄", name="杨逍").first()
print('单节点查询：\n',node_single)

## 按照label查询所有节点
node_hero = nodes.match("英雄").all()
print('查询结果的数据类型:',type(node_hero))

# 在查询结果中循环取值，用first()取出第一个值
i = 0
for node in node_hero:
    print('label查询第{}个为：{}'.format(i,node))
    i+=1

## 按照name查询所有节点：用all()取出所有值
node_name = nodes.match(name='张无忌').all()
print('name查询结果：',node_name)

# get（）方法按照id查询节点
node_id = nodes.get(1)
print('id查询结果：',node_id)

# 运行结果
# 单节点查询：
#  (_1:英雄 {name: '\u6768\u900d', 武力值: '100'})
# 查询结果的数据类型: <class 'list'>
# label查询第0个为：(_0:英雄 {name: '\u5f20\u65e0\u5fcc'})
# label查询第1个为：(_1:英雄 {name: '\u6768\u900d', 武力值: '100'})
# label查询第2个为：(_6:英雄 {name: '\u5f20\u7fe0\u5c71'})
# label查询第3个为：(_7:英雄 {name: '\u72ee\u738b'})
# label查询第4个为：(_8:英雄 {name: '\u6bb7\u7d20\u7d20'})
# name查询结果： [Node('英雄', name='张无忌')]
# id查询结果： (_1:英雄 {name: '\u6768\u900d', 武力值: '100'})

from py2neo import NodeMatch

nodess = NodeMatch(test_graph, labels=frozenset({'英雄'}))

# 遍历查询到的节点
print('=' * 15, '遍历所有节点', '=' * 15)
for node in iter(nodess):
    print(node)
# 查询结果计数
print('=' * 15, '查询结果计数', '=' * 15)
print(nodess.count())
# 按照武力值排序查询结果:注意引用字段的方式，前面要加下划线和点：_.武力值
print('=' * 10, '按照武力值排序查询结果', '=' * 10)
wu = nodess.order_by('_.武力值')
for i in wu:
    print(i)

# # 运行结果
# == == == == == == == = 遍历所有节点 == == == == == == == =
# (_10:英雄 {name: '\u72ee\u738b', 武力值: 100})
# (_11:英雄 {name: '\u6bb7\u7d20\u7d20'})
# (_17:英雄 {name: '\u5f20\u65e0\u5fcc'})
# (_18:英雄 {name: '\u6768\u900d', 武力值: '100'})
# (_23:英雄 {name: '\u5f20\u7fe0\u5c71'})
# == == == == == == == = 查询结果计数 == == == == == == == =
# 5
# == == == == == 按照武力值排序查询结果 == == == == ==
# (_18:英雄 {name: '\u6768\u900d', 武力值: '100'})
# (_10:英雄 {name: '\u72ee\u738b', 武力值: 100})
# (_11:英雄 {name: '\u6bb7\u7d20\u7d20'})
# (_17:英雄 {name: '\u5f20\u65e0\u5fcc'})
# (_23:英雄 {name: '\u5f20\u7fe0\u5c71'})

from py2neo import RelationshipMatcher
# 查询某条关系
relation = RelationshipMatcher(test_graph)

# None表示any node哦！不是表示空
print('=' * 10, 'hate关系查询结果', '=' * 10)
x = relation.match(nodes=None, r_type='hate')
for x_ in x:
    print(x_)
# 增加俩关系
re1_1 = Relationship(node_101, '情敌', node_102)
re1_2 = Relationship(node_102, '情敌', node_103)
test_graph.create(re1_1)
test_graph.create(re1_2)
# 情敌查询结果
print('=' * 10, 'hate关系查询结果', '=' * 10)
x = relation.match(nodes=None, r_type='情敌')
for x_ in x:
    print(x_)

# # 运行结果
# == == == == == hate关系查询结果 == == == == ==
# (周芷若) - [: hate
# {}]->(赵敏)
# == == == == == hate关系查询结果 == == == == ==
# (周芷若) - [: 情敌
# {}]->(小昭)
# (小昭) - [: 情敌
# {}]->(蛛儿)