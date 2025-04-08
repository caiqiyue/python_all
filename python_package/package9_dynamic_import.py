

import importlib
"""
根据字符串，动态导入模块
"""
module_name = 'math'

#使用第三方包动态导入
module = importlib.import_module(module_name)

#使用内置函数，动态导入
m = __import__(module_name)

print(module.sqrt(16))

print(m.sqrt(16))

# class Myclass(object):
#     x = 10
    
    
# print(__import__('Myclass'))