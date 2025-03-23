


import os
#os 是内置模块，如果 你自定义的模块 也叫 os ，那么会先从内置模块中去找，再去 sys.path 文件路径中去找
import sys

print(sys.path)
"""
['c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package', 'D:\\anconda\\envs\\pythonProject4\\python39.zip', 'D:\\anconda\\envs\\pythonProject4\\DLLs', 'D:\\anconda\\envs\\pythonProject4\\lib', 'D:\\anconda\\envs\\pythonProject4', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\hnswlib-0.6.1-py3.9-win-amd64.egg', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\win32', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\win32\\lib', 'D:\\anconda\\envs\\pythonProject4\\lib\\site-packages\\Pythonwin']
"""
#第一种：sys.path是一个列表，如果在内建模块中没有找到模块，就会更具这个列表里的顺序去找模块
#所以，假设有的模块找不到，你可以 sys.append("模块路径")，这样添加模块路径，但是这种用法仅限于本文件，也可以insert 加到列表最前面，提升她的优先级

#第二种：当然，也可以添加用户环境变量（模块所在的文件路径），这样也可以导入 模块；如果pycharm中没有识别到这个环境变量的话，就到interpreter中去修改（自己找视频看）

import site
print(site.getsitepackages())#pth就像配置文件一样，可以配置你需要导入的模块的路径，pth文件放在site列表中的任意一个路径中都可以生效

#第三种：添加pth文件，比如在python36根目录下，如果是anconda，那就再env的项目根目录下，添加pth文件，文件内部写上你需要的模块的所在文件的路径

print(sys.modules)#打印已经加载的模块，第二次导入并不会重新导入，从这个已经加载的所有模块中去找