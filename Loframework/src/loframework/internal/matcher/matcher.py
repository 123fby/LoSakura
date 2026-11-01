from loframework.internal.adapter import Event
from collections.abc import Callable, Iterable
from functools import wraps
from typing import Any,Dict
from loguru import logger
class HandlerTask:
    """函数处理队列"""
    def __init__(self,func:Callable,parameterless:Iterable[ Any]|None=None):
        self.func = func
        self.signal:bool = False
        self.parameterless = parameterless
    def is_completed(self):
        return self.signal
class Matcher:
    REGISTED_MATCHERS:Dict[str,Matcher] = {}
    @classmethod
    def __register(cls,matcher:Matcher):
        cls.REGISTED_MATCHERS.update({matcher.bot_name:matcher})
    @classmethod
    def register_matcher(cls,bot_name:str):
        cls.__register(cls(bot_name))
        return bot_name
    def __init__(self,bot_name:str):
        self.dict:Dict[str,HandlerTask] ={}
        self.bot_name = bot_name
    @classmethod
    def handle(cls,bot_name:str,parameterless:Iterable[ Any]|None=None):
        """将一个函数加入到处理队列中"""
        def wrapper(func:Callable[[Matcher, Event ], None]):
            macther = cls.REGISTED_MATCHERS[bot_name]
            macther.appended_dict(HandlerTask(func,parameterless=parameterless)) 
            """不修改func,只将func的引用添加到dict中"""
            return func
        return  wrapper
    
    def send(self,msg:str):
        print(f"AI:hi!{msg}")         
    async def handle_task(self,event: Event)-> None:
        for task in self.dict.values():
            logger.debug(f"正在执行{task.func.__name__}")
            await task.func(self,event)
    def appended_dict(self,HandlerTask:HandlerTask):
        self.dict[HandlerTask.func.__name__] = HandlerTask
    @classmethod
    async def dispatch(cls,bot_name:str,event:Event):
        """将事件分发到对应的处理队列中"""
        macther = cls.REGISTED_MATCHERS[bot_name]
        await macther.handle_task(event)
