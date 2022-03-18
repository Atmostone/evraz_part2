from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import User, Chat


class UsersRepo(ABC):
    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User):
        ...


class ChatsRepo(ABC):
    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def add(self, chat: Chat):
        ...


# class ChatUsersRepo(ABC):
#
#     @abstractmethod
#     def get_by_id(self, id_: int) -> Optional[ChatUser]:
#         ...
#
#     @abstractmethod
#     def add(self, chat_user: ChatUser):
#         ...
#
#
# class MessagesRepo(ABC):
#
#     @abstractmethod
#     def get_by_id(self, id_: int) -> Optional[Message]:
#         ...
#
#     @abstractmethod
#     def add(self, message: Message):
#         ...
