from loframework.adapters import Adapter,Matcher
from typing import override, Callable
from loguru import logger
from .message import Message
from .event import Event
import asyncio
class ConsoleAdapter(Adapter):
    def __init__(self):
        self.running : bool = True
    @override
    async def run(self):
        print("Hello from console adapter")
        while self.running:
            try:

                res=await asyncio.to_thread(self.get_message)
                res = Message.create_msg(res)
            except asyncio.CancelledError:
                self.running = False
                break
            event = Event(res)
            await Matcher.dispatch(event.event_data
                                   .bot_name,event)
            if res == "exit":
                self.running = False
            
    def get_message(self):
        message = input("Enter message: ")
        return message
    @override
    def get_adapter(self)->ConsoleAdapter:
        return self
