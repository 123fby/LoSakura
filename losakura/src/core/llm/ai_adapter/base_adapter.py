from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .custom_error import ChatError

class BaseAdapter(ABC):
    async def _chat(self,model:str=None,
        messages:list[str]=None,temperature:float=0.7,
        max_tokens:int=1024,top_p:float=0.9,**kwargs) ->str:
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
                return response.choices[0].message.content.strip() 
            except Exception as e:
                raise ChatError(e)
    async def chat(self,**kwargs)->str|bool:
        try:
            response=await self._chat(**kwargs)
            return response
        except ChatError as e:
            print(e)
            return False