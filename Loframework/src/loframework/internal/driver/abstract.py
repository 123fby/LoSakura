from abc import ABC , abstractmethod
from typing import Any,List
from .lifespan import LifeSpan
class Driver(ABC):
    registered_items:List[Any] = []
    @abstractmethod
    def run(self):
        """驱动程序运行"""
    @abstractmethod
    def get_driver(self)->Driver:
        """获取驱动程序"""
    @abstractmethod
    def load_adapter(self,adapter_name:str):
        """加载适配器"""
    # @abstractmethod
    # def load_plugin(self,plugin_name:str):
    #     """加载插件"""
    async def lifespan_start(self):
        """生命周期开始"""
        await LifeSpan.start()
    async def lifespan_stop(self):
        """生命周期结束"""
        await LifeSpan.stop()
    def lifespan_register(self,item:type):
        """注册一个对象"""
        LifeSpan.register(item)
    def lifespan_get(self,name:str=None)->type|None:
        """获取生命周期中的对象"""
        return LifeSpan.get_registered(name=name)