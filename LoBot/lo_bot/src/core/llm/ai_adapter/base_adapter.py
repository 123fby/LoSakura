from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseAdapter(ABC):
    async def chat(self,model:str=None,
        messages:list[str]=None,temperature:float=0.7,
        max_tokens:int=1024,top_p:float=0.9,**kwargs) ->str|bool:
            msg=messages
            model=model or self.model
            self.model=model      
            try:
                response=await self.client.chat.completions.create(
                model=model,
                messages=msg,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                **kwargs
                    )
                return response
            except Exception as e:
                 pass