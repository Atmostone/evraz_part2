from typing import List, Optional

import attr


@attr.dataclass
class User:
    username: str
    password: str
    id: Optional[int] = None


@attr.dataclass
class Chat:
    info: str
    owner: int
    id: Optional[int] = None


@attr.dataclass
class ChatUser:
    id: int
    user: int
    chat: int


@attr.dataclass
class Message:
    id: int
    user: int
    chat: int
    text: str
