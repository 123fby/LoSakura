from typing import Any,Dict,List,Protocol,Coroutine

from loguru import logger

class LifeSpanItem(Protocol):


    @classmethod
    async def create(cls,**kwargs)->LifeSpanItem:
        ...
    async def start(self):
        ...
    async def stop(self):
        ...
class LifeSpan:
    registeredDict:Dict[str,LifeSpanItem]={}
    registeredList:List[LifeSpanItem | Coroutine[Any,Any,LifeSpanItem]]=[]
    # registeredDictMap:Dict[LifeSpanItem,str]
    @classmethod
    def register(cls,Item:type[LifeSpanItem],**kwargs):
        """存储协程item.create"""
        item=Item.create(**kwargs)
        cls.registeredList.append(item)
        # cls.registeredDictMap[item]=item.__name__
        logger.info(f"Register {item} Coroutine for lifespan")
    @classmethod
    async def start(cls):
        for index,item in enumerate(cls.registeredList):
            """get item from Coroutine"""
            item=await item 
            cls.registeredDict[item.__name__]=item
            cls.registeredList[index]=item
            logger.info(f"Start {item.__name__} for lifespan")
            await item.start()
    @classmethod
    async def stop(cls):
        for item in reversed(cls.registeredList):
            logger.info(f"Stop {item.__name__} for lifespan")
            await item.stop()
    @classmethod
    def get_registered(cls,name:str=None)->LifeSpanItem|None:
        return cls.registeredDict.get(name)