from typing import Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from components.chat_backend.chat.application.dataclasses import User, Chat
from components.chat_backend.chat.application.interfaces import UsersRepo, ChatsRepo


@component
class UsersRepo(BaseRepository, UsersRepo):
    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()

        return user


@component
class ChatsRepo(BaseRepository, ChatsRepo):
    def get_by_id(self, id_: int) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat: Chat):
        print('4')
        self.session.add(chat)
        print('5')
        self.session.flush()

        return chat
