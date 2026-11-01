from pydantic import BaseModel,Field
from typing import List,Any
from .message import Message
import uuid
class EventData(BaseModel):
    message:Message|None
    user_id:int = 0
    message_id:str|None=None
    user_name:str = "Kerin"
    bot_name:str = "Lolo"
    message_type :List[str]=Field(default=["console","LoUI","qqPrivate","qqGroup"])
class Event:
    def __init__(self,message:Message|None=None,**kwargs):
        self.event_data:EventData = EventData(message=message,**kwargs)
        self.create_uuid()
    @property
    def msg_parser(self)->Message:
        """获取message对象  """
        return self.event_data.message  
    def is_None(self)->bool:
        return self.event_data.message is None
    def create_uuid(self)->None:
        if self.event_data.message_id is None:
            self.event_data.message_id = str(uuid.uuid4())
    def to_dict(self)->dict:
        temp= self.event_data.__dict__
        temp["message"] = temp["message"].get_message() 
        return temp
    @property
    def event_data(self)->EventData:
        return self.event_data
