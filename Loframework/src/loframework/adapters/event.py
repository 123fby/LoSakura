from loframework.internal.adapter import EventData as BaseEventData
from loframework.internal.adapter import Event as EventBase
from .message import Message
from pydantic import BaseModel
from typing import override
class EventData(BaseEventData):
    pass
class Event(EventBase):
    def __init__(self,message:Message|None=None,**kwargs):
        self.event_data:EventData = EventData(message=message,**kwargs)
        self.create_uuid()
    @override
    @property
    def msg_parser(self)->Message:
        """获取message对象  """
        return self.event_data.message  
    @override
    def is_None(self)->bool:
        return self.event_data.message is None