from loframework.internal.adapter import Message as BaseMessage
from typing import override
class Message[T](BaseMessage[T]):
    message: T
    @override
    def get_message(self)-> T:
        return self.message