

from py2neo import Graph,Node,Relationship
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456"))
graph.delete_all()
# 定义node
node_1 = Node('英雄',name = '张无忌')
node_2 = Node('英雄',name = '杨逍',武力值='100')
node_3 = Node('派别',name = '明教')

# 存入图数据库
graph.create(node_1)
graph.create(node_2)
graph.create(node_3)
print(node_1)


# 增加关系
node_1_to_node_2 = Relationship(node_2,'教主',node_1)
node_3_to_node_1 = Relationship(node_1,'统领',node_3)
node_2_to_node_2 = Relationship(node_2,'师出',node_3)

graph.create(node_1_to_node_2)
graph.create(node_3_to_node_1)
graph.create(node_2_to_node_2)

