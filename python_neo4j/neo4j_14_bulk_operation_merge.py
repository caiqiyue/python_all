

from py2neo import*
from py2neo.bulk import merge_nodes,create_nodes

g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
g.delete_all()

keys = ['name','age']

data = [
    ['caiqiyue',20],
    ['bob',10],
    ['candy',10],
    ['caiqiyue',22],
    ['cyiel',29],
    ['candy',18]
]


merge_nodes(g.auto(),data,('Person','age'),keys=keys)
"""
tx – Transaction in which to carry out this operation

data – node data supplied as a list of lists (if keys are provided) or a list of dictionaries (if keys is None)

merge_key – tuple of (label, key1, key2…) on which to merge  根据 key 去重或者说就融合

labels – additional labels to apply to the merged nodes

keys – optional set of keys for the supplied data (if supplied as value lists)

preserve – optional set of keys that designate property values to preserve in nodes that already exist


"""


print(g.nodes.match("Person").count())

print('over')