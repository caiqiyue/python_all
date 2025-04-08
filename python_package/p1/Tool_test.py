
#仍需要注意 python2中所有的包内导入，都是相对导入，如果要破除相对导入 需要先 from __future__ import absolute_import
# import Tool3
from . import Tool3# 包内导入使用相对导入，不容易出错；但是注意，使用相对导入的时候，如果Tool_test被当作脚本运行，就会报错
"""
但有需要注意的是， 这个点 .  不一定是Tool_test文件所在的目录p1

比如这个模块 被当做脚本运行的时候 它的名称是 __main__
如果 它是被其他模块导入 而运行的话， 它的名称 是   包名.子包名.模块 ， 包名 又称为顶级名称

Tool_test被当做脚本运行的时候，文件名称 是 __main__ 所以不存在 from . import Tool3，这个 .  找不到它对应的目标
只有 在被当做 模块导入运行的时候 不会报错
  
"""


import sys

# print(sys.path)

"""
['c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package\\p1', 'D:\\anconda\\envs\\pythonProject4\\python39.zip', 'D:\\anconda\\envs\\pythonProject4\\DLLs', 'D:\\anconda\\envs\\pythonProject4\\lib', 'D:\\anconda\\envs\\pythonProject4', 'C:\\', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\hnswlib-0.6.1-py3.9-win-amd64.egg', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\win32', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\win32\\lib', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\Pythonwin']
Tool_test这个模块，是p1包里面的模块，现在我从Tool_test中，导入 p1 包里面的Tool，属于包里面导入模块
打印sys.path
可以看到模块的查找路径优先级的排序，第一 路径是 'c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package\\p1' 
这个Tool_test当前模块所在的目录
所以，你导入Tool模块的时候，它就会先去 这个路径（...p1）下去找Tool，那么这个路径下也的确存在Tool模块

注意，包内导入的时候，使用绝对导入，容易出现问题；也就是包外的文件导入Tool_test,Tool_test使用绝对导入，导入包内模块，可能会出现报错
所以包内导入，最好用相对导入

"""

print(__name__)