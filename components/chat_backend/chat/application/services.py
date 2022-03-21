from typing import Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments
from datetime import datetime

from components.chat_backend.chat.application import interfaces, dataclasses
from components.chat_backend.chat.application.dataclasses import ChatUser
from components.chat_backend.chat.application.exceptions import NotAllowed, DoesNotExists, AuthFailed

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    username: str
    password: str


class ChatInfo(DTO):
    id: Optional[int]
    info: str
    owner: int
    title: str


class ChatUserInfo(DTO):
    id: Optional[int]
    user: int
    chat: int


class MessageInfo(DTO):
    id: Optional[int]
    user: int
    chat: int
    text: str
    datetime: datetime


@component
class User:
    users_repo: interfaces.UsersRepo

    @join_point
    @validate_arguments
    def login(self, username: str, password: str):
        user = self.users_repo.get_by_login(username, password)
        if not user:
            raise AuthFailed
        return user

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        user = user_info.create_obj(dataclasses.User)
        self.users_repo.add(user)


@component
class Chat:
    chats_repo: interfaces.ChatsRepo
    chat_user_repo: interfaces.ChatUsersRepo

    def chat_exist(self, chat_id):
        try:
            chat = self.chats_repo.get_by_id(chat_id)
        except Exception:
            raise DoesNotExists
        return chat

    def user_in_chat(self, chat_id, user_id):
        user = self.chat_user_repo.check_user(chat_id, user_id)
        if user is None:
            raise DoesNotExists
        return user

    @join_point
    @validate_arguments
    def get_users(self, token, chat_id):
        try:
            self.user_in_chat(chat_id, token)
        except Exception:
            raise NotAllowed
        else:
            users = self.chat_user_repo.get_users(chat_id)
            return users

    @join_point
    @validate_arguments
    def get_info(self, token, chat_id):
        try:
            self.user_in_chat(chat_id, token)
        except Exception:
            raise NotAllowed
        else:
            chat = self.chats_repo.get_by_id(chat_id)
            if not chat:
                raise DoesNotExists
            return chat

    @join_point
    @validate_arguments
    def add_chat(self, owner, title, info):
        chat = ChatInfo(owner=owner, title=title, info=info).create_obj(dataclasses.Chat)
        self.chats_repo.add(chat)
        self.chat_user_repo.add(ChatUser(chat=chat.id, user=chat.owner))

    @join_point
    @validate_arguments
    def modify_chat(self, token, id, title, info, owner):
        try:
            self.user_in_chat(id, token)
        except Exception:
            raise NotAllowed
        else:
            try:
                chat = self.chats_repo.get_by_id(id)
            except Exception:
                raise DoesNotExists
            chat_info = ChatInfo(id=id, title=title, info=info, owner=owner)
            chat_info.populate_obj(chat)

    @join_point
    @validate_arguments
    def delete_chat(self, token, id):
        try:
            self.user_in_chat(id, token)
        except Exception:
            raise NotAllowed
        else:
            try:
                self.chats_repo.get_by_id(id)
            except Exception:
                raise DoesNotExists
            self.chats_repo.delete(id)

    @join_point
    @validate_arguments
    def join_chat(self, user_id, chat_id):
        try:
            self.user_in_chat(chat_id, user_id)
        except Exception:
            new_row = ChatUserInfo(chat=chat_id, user=user_id).create_obj(ChatUser)
            self.chat_user_repo.add(new_row)

    @join_point
    @validate_arguments
    def leave_chat(self, token, chat_id):
        try:
            self.user_in_chat(chat_id, token)
        except Exception:
            raise NotAllowed
        else:
            self.chat_user_repo.leave(chat_id, token)


@component
class Message:
    chats_repo: interfaces.ChatsRepo
    chat_user_repo: interfaces.ChatUsersRepo
    message_repo: interfaces.MessageRepo

    def user_in_chat(self, chat_id, user_id):
        user = self.chat_user_repo.check_user(chat_id, user_id)
        if user is None:
            raise DoesNotExists
        return user

    @join_point
    @validate_arguments
    def write_message(self, token, chat_id, text):
        try:
            self.user_in_chat(chat_id, token)
        except Exception:
            raise NotAllowed
        else:
            message = MessageInfo(user=token, chat=chat_id, text=text, datetime=datetime.now()).create_obj(
                dataclasses.Message)
            self.message_repo.add(message)

    @join_point
    @validate_arguments
    def get_message(self, token, chat_id):
        try:
            self.user_in_chat(chat_id, token)
        except Exception:
            raise NotAllowed
        else:
            return self.message_repo.get_by_id(chat_id)
