from plugininterface import PluginInterface

# 插件管理器
class PluginManager:
    def __init__(self):
        self.plugins = {}
 
    def load_plugins(self, plugin_module_names):
        for module_name in plugin_module_names:#plugin1 模块名称，即py文件名称
            try:
                # 动态加载模块
                module = __import__(module_name)#导入plugin1 相当于 import plugin1
                
                # 遍历模块的成员
                for member_name in dir(module):#import plugin1 文件执行一遍plugin1.py，同时创建 module对象，将plugin1.py文件中的所有资源作为属性绑定在module对象身上，dir(module)就是获取plugin1模块中的所有属性和方法，只有类Plugin1
                    member = getattr(module, member_name)#从plugin1模块中，获取 属性   类Plugin1  所以member就是  plugin1.Plugin1  此时相当于  from plugin1 import Plugin1
                    
                    # 检查成员是否为插件实现类
                    if (
                        isinstance(member, type)#是否是由元类创建
                        and issubclass(member, PluginInterface)#是否是实现了 接口  的 类
                        and member != PluginInterface# 不是 接口 本身
                    ):
                        # 创建插件实例
                        plugin = member()#实例化 Plugin1  plugin = Plugin1()
                        
                        # 注册插件
                        self.plugins[module_name] = plugin  #self.plugins :  {'plugin1':plugin}
            except ImportError:
                print(f"无法加载模块：{module_name}")
 
    def run_plugins(self):
        for module_name, plugin in self.plugins.items():#'plugin1',plugin
            print(f"Running plugin from module: {module_name}")
            plugin.run()#执行 plugin1对象中的run方法
 
# 主程序
if __name__ == "__main__":
    # 创建插件管理器
    manager = PluginManager()
    
    # plugin1 = Plugin1()
    # plugin2 = Plugin2()
    # 加载插件模块
    manager.load_plugins(["plugin1", "plugin2"])
 
    # 运行插件
    manager.run_plugins()