from py2neo import *
from py2neo.bulk import create_nodes


g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()


# 第一种 数据 结构  属性和属性值分开，就以列表的形式 传递
keys = ['name','age']

data = [
    ['caiqiyue',20],
    ['bob',29],
    ['candy',10]
]
create_nodes(g.auto(),data,labels={'Person'},keys=keys)#批量，创建节点

print(g.nodes.match('Person').count())


#第二种  可以 传入的 数据结构  属性和属性值对应，就以字典的形式
teacher = [
    {"name": "Dave", "age": 66},
    {"name": "Eve", "date_of_birth": "1943-10-01"},
    {"name": "Frank"},
]

create_nodes(g.auto(),teacher,labels={'Teacher'})

print(g.nodes.match('Teacher').count())

#第三种，切分数据，一批一批的创建节点

women = [
    {"name": "Dave", "age": 66},
    {"name": "Eve", "date_of_birth": "1943-10-01"},
    {"name": "Frank"},
    {"name": "Candy", "age": 66},
    {"name": "BOB", "date_of_birth": "1943-10-01"},
    {"name": "Cacy"},
    {"name": "Devie", "age": 66},
    {"name": "Orcal", "date_of_birth": "1943-10-01"},
    {"name": "Vady"},
    
]

from itertools import islice
stream = iter(women)
batch_size = 3
while True:
    batch = islice(stream, batch_size)
    if batch:
        create_nodes(g.auto(), batch, labels={"Person"})
        print(g.nodes.match("Person").count())
    else:
        break