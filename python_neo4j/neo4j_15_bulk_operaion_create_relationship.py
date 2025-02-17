from py2neo import*
from py2neo.bulk import merge_nodes,create_nodes,create_relationships

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()



person_keys = ["name", "age"]
person = [
    ["Alice", 33],
    ["Bob", 44],
    ["Carol", 55],
]

company_keys = ['name']
company = [
    ['ACME'],['Bob Corp'],['The Daily Planet']
]


create_nodes(g.auto(),person,labels={'Person'},keys=person_keys)
create_nodes(g.auto(),company,labels={'Company'},keys=company_keys)

data = [
    (("Alice", 33), {"since": 1999}, "ACME"),
    (("Bob", 44), {"since": 2002}, "Bob Corp"),
    (("Carol", 55), {"since": 1981}, "The Daily Planet"),
]
create_relationships(g.auto(), data, "WORKS_FOR", \
    start_node_key=("Person", "name", "age"), end_node_key=("Company", "name"))
"""
# data 的构造是
# [((开始节点属性1，开始节点属性2)，{关系节点属性：属性值}，（结束节点属性1，属性2）)]



start_node_key = (label,key1,key2) = end_node_key

而且也需要注意，如果没有 开始节点和结束节点，他不会创建新的节点

"""

#如果已知结束节点的id值，也可以直接使用id值来
data = [
    (("Alice", "Smith"), {"since": 1999}, 123),
    (("Bob", "Jones"), {"since": 2002}, 124),
    (("Carol", "Singer"), {"since": 1981}, 201),
]
create_relationships(g.auto(), data, "WORKS_FOR", \
    start_node_key=("Person", "name", "family name"))
