from typing import Optional

import attr
from sqlalchemy import DateTime


@attr.dataclass
class User:
    username: str
    password: str
    id: Optional[int] = None


@attr.dataclass
class Chat:
    info: str
    title: str
    owner: int
    id: Optional[int] = None


@attr.dataclass
class ChatUser:
    user: int
    chat: int
    id: Optional[int] = None


@attr.dataclass
class Message:
    user: int
    chat: int
    text: str
    datetime: DateTime
    id: Optional[int] = None