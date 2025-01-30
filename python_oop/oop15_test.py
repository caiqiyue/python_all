import oop15_public_attribute_access 

#跨模块访问 公有属性  或者 公有变量
print(oop15_public_attribute_access.v)

#公有属性   还可以  这样  跨模块 访问
from oop15_public_attribute_access import *
print(v)



import oop15_protected_attribute_access

#跨模块访问  受保护属性 或者 受保护变量
print(oop15_protected_attribute_access._v)

#受保护属性就不可以 这样    跨模块访问 ，因为受保护属性不会被导入到另一个模块中，只有  模块.受保护属性  这样访问, 除非  __all__ =[] 指名受保护属性可以被导入
from oop15_protected_attribute_access import *
print(_v)

