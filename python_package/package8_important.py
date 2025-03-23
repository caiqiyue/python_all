




"""
你在项目当中，经常会出现，明明有这个包，但是导入的时候，总是显示包不存在

首先，导入有两种情况，在包里面的文件导入包里面的模块；包外面的文件导入包里面的模块

针对于，在包里面导入模块，就会有 绝对导入  和 相对导入
 . 表示当前文件所在的目录 .. 表示当前文件所在的上一级目录 
 
 
当前文件，想导入，p1包下的模块，属于 包外面的文件导入包内部的模块
可以看到 当前文件 执行的时候， 会先将，当前文件所在的目录 添加到 sys.path中去，所以肯定先从这里面去查找模块
'c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package'

这个路径下，存在p1包，所以可以导入p1包，所以还可以从p1中再次导入 Tool_test模块

但是现在就会报错了，找不到Tool3模块

因为我们导入了Tool_test模块，会去执行Tool_test里面的内容，该模块要求导入Tool3模块
但是 我们现在是 在 p1包外面执行程序，sys.path的路径是 'c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package'

在执行到Tool_test中导入Tool3模块的语句时，它的sys.path 是 'c:\\Users\\ASUS\\PycharmProjects\\python_all\\python_package'
而这个路径下是没有 Tool3文件的，所以会找不到Tool3模块

这个问题你以前经常碰到，所以导入的时候，需要注意一下，包内导入，还是包外导入
"""
from p1 import Tool_test
#p1.Tool_test  Tool_test文件是被导入的时候执行的，所以 Tool_test文件  名称是  p1.Tool_test  包名.模块
#那么我们在 Tool_test 模块中 写 from . import Tool3  这个 .  就是 Tool_test前面一级 p1的路径，所以要是 写 from .. import Tool3 就会报错，因为 Tool_test的文件名称是 p1.Tool_test；那按照你之前的理解 一个点  .  代表 p1 两个点 .. 代表就是p1的上一级目录，但这是错的
#一定要注意，不要把 相对导入 的  .   当做当前文件所在的目录  这个 .  一定要根据  运行时的文件名称来判断



print(__name__)#__main__,这个文件是 脚本运行 所以 名称是 __main__

import sys

# print(sys.path)


