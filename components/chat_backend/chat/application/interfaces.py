from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import User, Chat, ChatUser, Message


class UsersRepo(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]:
        ...

    @abstractmethod
    def get_by_login(self, username: str, password: str) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User):
        ...


class ChatsRepo(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def add(self, chat: Chat):
        ...

    @abstractmethod
    def delete(self, chat: Chat):
        ...


class ChatUsersRepo(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[ChatUser]:
        ...

    @abstractmethod
    def get_users(self, id: int):
        ...

    @abstractmethod
    def add(self, chat_user: ChatUser):
        ...

    def check_user(self, chat_id: int, user_id: int):
        ...

    @abstractmethod
    def leave(self, chat_id, user_id):
        ...

class MessageRepo(ABC):
    @abstractmethod
    def get_by_id(self, chat_id: int):
        ...

    @abstractmethod
    def add(self, message: Message):
        ...
