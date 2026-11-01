from pydantic import BaseModel
from abc import ABC, abstractmethod
class Message[T](BaseModel, ABC):
    @abstractmethod
    def get_message(self)->T:
        """返回message内容"""
    @classmethod
    def create_msg(cls,message: T, **kwargs):
        return cls(message=message,**kwargs)