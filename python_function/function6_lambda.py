



"""
lambda 本身就是一个函数，所以可以加上 小括号，使用该函数
当然，也可以给他绑定一个函数名
"""
res = (lambda x,y:x+y)(1,2)
print(res)

newFunc = lambda x,y:x-y
print(newFunc(3,4))


l = [{'name':'caiqiyue','age':10},{'name':"xxxx",'age':1}]

rs = sorted(l,key=lambda x:x['age'])
print(rs)