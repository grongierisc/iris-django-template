from iop import Message
from dataclasses import dataclass

@dataclass
class HttpMessageRequest(Message):
    method: str
    url: str
    headers: dict
    body: str

@dataclass
class HttpMessageResponse(Message):
    status: int
    headers: dict
    body: str