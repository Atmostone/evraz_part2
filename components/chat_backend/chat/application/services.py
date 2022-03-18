from typing import Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from components.chat_backend.chat.application import interfaces, dataclasses

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


class ChatInfoForChange(DTO):
    id: int
    info: str = None
    owner: int = None
    title: str = None


@component
class User:
    users_repo: interfaces.UsersRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        user = self.users_repo.get_by_id(id)
        if not user:
            raise Exception
        return user

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        user = user_info.create_obj(dataclasses.User)
        self.users_repo.add(user)


@component
class Chat:
    chats_repo: interfaces.ChatsRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        chat = self.chats_repo.get_by_id(id)
        if not chat:
            raise Exception
        return chat

    @join_point
    @validate_with_dto
    def add_chat(self, chat_info: ChatInfo):
        chat = chat_info.create_obj(dataclasses.Chat)
        self.chats_repo.add(chat)

    @join_point
    @validate_with_dto
    def modify_chat(self, chat_info: ChatInfoForChange):
        id = chat_info.id
        try:
            chat = self.chats_repo.get_by_id(id)
        except TypeError:
            raise Exception
        chat_info.populate_obj(chat)
