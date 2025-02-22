from py2neo import *
from py2neo.cypher.queries import unwind_create_nodes_query
g = Graph("http://localhost:7474", auth=("neo4j", "12345678"))
g.delete_all()

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {'name':'Charlie','age':10}
]

labels = ["Person"]

query = unwind_create_nodes_query(data, labels)#自动生成，创建节点的 query语句，但是 query是一个元组（语句，数据）
g.run(query[0],{'data':data})#批量创建节点
print(query[0])