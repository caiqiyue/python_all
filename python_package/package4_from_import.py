


from p1.sub_p1.Tool2 import *
# Tool2这个模块下，有很多资源，但只会 导入 __all__ =【】里面定义的资源,而且也不会导入 受保护资源 比如 _num5,这种受保护资源只能手动导入

from p1.sub_p1.Tool2 import num3,_num5 # 不在 __all__ 列表中的资源可以手动导入


print(num1)
print(num2)
print(_num5)#
#print(num3) 虽然 该模块中有 这个num3资源，但是它没有被定义在 __all__列表中，所有 在  import *  的时候不会被导入


#和上面 从 模块中导入资源同理，现在是从包中导入模块，会根据模块__init__文件中的__all__列表来导入
from p1.sub_p1 import *

print(Tool1.name)
print(Tool2.num1)
#print(Tool3.name)这个包里面有Tool3模块，但是 __all__中没有被定义，所以就不会被导入


