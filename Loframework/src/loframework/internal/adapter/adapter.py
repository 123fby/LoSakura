from abc import ABC, abstractmethod

class Adapter(ABC):
    @abstractmethod
    def run(self):
        """启动适配器"""
    @abstractmethod
    def get_adapter(self)->Adapter:
        """获取适配器实例"""

