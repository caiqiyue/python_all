

from py2neo import Graph,Node
#链接数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456"))
graph.delete_all()

# 定义node
node_1 = Node('英雄',name = '张无忌')


#节点的一些关于标签的函数 ================================================================

print(set(node_1.labels))#返回该节点所有的标签   {'英雄'}

node_1.add_label("杀手")#为该节点增加标签 
print(set(node_1.labels))#{'杀手', '英雄'}

print(node_1.has_label("人物"))#返回该节点是否有这个标签

node_1.remove_label("英雄")#删除该节点的标签
print(node_1.labels)

node_1.clear_labels()#清空该节点所有标签
print(node_1.labels)

node_1.update_labels(['英雄','杀手'])#根据可迭代对象，添加多个标签
print(node_1.labels)


#节点的一些关于属性的函数=====================================================
print("=================================================================================")
print(node_1['name'])#返回节点的某一属性值


node_1['name'] = '蔡启越'#为属性赋值
print(node_1['name'])


print(len(node_1))#返回属性个数

print(dict(node_1))#返回 属性的  键值对   {'name': '蔡启越'}

print(node_1.get('name'))#使用get函数，返回属性值

print(node_1.items())#dict_items([('name', '蔡启越')])  (key,value),(),

print(node_1.keys())#dict_keys(['name'])

print(node_1.values())#dict_values(['蔡启越'])

node_1.setdefault('age',default=20) #如果该属性已存在，则返回该属性值；若没有该属性，则用默认值设置属性值
print(node_1.items())#dict_items([('name', '蔡启越'), ('age', 20)])

node_1.update({'name':'casasd'})#更新属性值，可以多属性一起更新
print(node_1['name'])



