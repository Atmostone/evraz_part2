from typing import Optional, List

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select, and_

from components.chat_backend.chat.application.dataclasses import User, Chat, ChatUser, Message
from components.chat_backend.chat.application.interfaces import UsersRepo, ChatsRepo, ChatUsersRepo, MessageRepo


@component
class UsersRepo(BaseRepository, UsersRepo):
    def get_by_id(self, id: int) -> Optional[User]:
        query = select(User).where(User.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def get_by_login(self, username: str, password: str) -> Optional[User]:
        query = select(User).where(and_(User.username == username, User.password == password))
        print('!!!!!!!!!!', self.session.execute(query).scalars().one_or_none())
        return self.session.execute(query).scalars().one_or_none()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()
        return user


@component
class ChatsRepo(BaseRepository, ChatsRepo):
    def get_by_id(self, id: int) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, chat: Chat):
        self.session.add(chat)
        self.session.flush()
        return chat

    def delete(self, id: int):
        query = select(Chat).where(Chat.id == id)
        self.session.delete(self.session.execute(query).scalars().one_or_none())


@component
class ChatUsersRepo(BaseRepository, ChatUsersRepo):
    def get_by_id(self, id: int) -> Optional[User]:
        pass

    def add(self, chatuser: ChatUser):
        self.session.add(chatuser)
        self.session.flush()
        return chatuser.id

    def leave(self, chat_id, user_id):
        query = select(ChatUser).where(Chat.id == chat_id, ChatUser.id == user_id)
        res = self.session.execute(query).scalars().one_or_none()
        self.session.delete(res)
        self.session.flush()

    def get_users(self, chat_id: int):
        query = select(ChatUser).where(Chat.id == chat_id)
        return self.session.execute(query).scalars().all()

    def check_user(self, chat_id: int, user_id: int):
        query = select(ChatUser).where(ChatUser.id == chat_id, ChatUser.id == user_id)
        return self.session.execute(query).scalars().one_or_none()


@component
class MessageRepo(BaseRepository, MessageRepo):

    def get_by_id(self, chat_id: int):
        query = select(Message).where(Message.chat == chat_id)
        return self.session.execute(query).scalars().all()

    def add(self, message: Message):
        self.session.add(message)
        self.session.flush()
        return message.id
