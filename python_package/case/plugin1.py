# 插件实现类1

from plugininterface import PluginInterface
class Plugin1(PluginInterface):
    def run(self):
        print("Running Plugin 1")