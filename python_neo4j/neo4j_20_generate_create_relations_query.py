from py2neo import Graph
from py2neo.cypher.queries import unwind_create_relationships_query

# 连接到 Neo4j 数据库
g = Graph("http://localhost:7474", auth=("neo4j", "12345678"))
# g.delete_all()

# 要插入的关系数据
data = [
    {"start_node": "Alice", "end_node": "Bob", "since": 2020},
    {"start_node": "Bob", "end_node": "Charlie", "since": 2021},
    {"start_node": "Alice", "end_node": "Charlie", "since": 2022}
]
# print(data[1][0])

rel_type = "KNOWS"#关系类型
start_node_key = 'Person'#开始节点的 属性
end_node_key = "Person"#结束节点的属性
keys = ["since"]#关系 属性

# 创建查询
query = unwind_create_relationships_query(data, rel_type, start_node_key, end_node_key, keys)
#query是一个元组
"""
('UNWIND $data AS r
    MATCH (a:name)   #这就是 批量创建关系失败的原因  name是属性，但被当作了标签，不知如何修改
    MATCH (b:name)
    CREATE (a)-[_:KNOWS]->(b)
    SET _ += {since: r[1][0]}', 
{'data': [{'start_node': 'Alice', 'end_node': 'Bob', 'since': 2020}, 
          {'start_node': 'Bob', 'end_node': 'Charlie', 'since': 2021}, 
          {'start_node': 'Alice', 'end_node': 'Charlie', 'since': 2022}]}
)


UNWIND $data AS rel_data
MATCH (start:Person {name: rel_data.start_node})
MATCH (end:Person {name: rel_data.end_node})
CREATE (start)-[r:KNOWS]->(end)
SET r.since = rel_data.since
UNWIND $data AS rel_data: 这个操作会将 data 列表中的每个字典展开，每个字典都会成为 rel_data。
MATCH (start:Person {name: rel_data.start_node}): 这行代码会根据 rel_data.start_node 查找起始节点。
MATCH (end:Person {name: rel_data.end_node}): 这行代码会根据 rel_data.end_node 查找目标节点。
CREATE (start)-[r:KNOWS]->(end): 创建一个类型为 KNOWS 的关系。
SET r.since = rel_data.since: 为关系 r 设置 since 属性。

"""

# 打印生成的查询，检查是否正确
print(query)

# 执行查询
# g.run(query[0], {"data": data})

# print("关系创建成功!")