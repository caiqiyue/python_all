


#这是标准库，下载python时，会自动下载，但调用时还是需要我们手动导入包
import os

#这是内置库，python会自动导入的包，比如int(),print(),float()等，就是它提供的
import builtins


builtins.print("xxx")


#导入自定义的包，自定义python包，必须包含__init__文件，而且导入这个包的时候，会自动执行__init__文件
import p1.Tool
print(p1.Tool.num)

import p1.sub_p1