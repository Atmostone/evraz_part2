from typing import List, Optional

import attr


@attr.dataclass
class User:
    id: int
    username: str
    password: str


@attr.dataclass
class Chat:
    id: int
    info: str
    creator: int


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
