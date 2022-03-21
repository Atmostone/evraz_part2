import json

from classic.components import component

from .join_points import join_point
from ...application import services


@component
class User:
    user: services.User

    @join_point
    def on_post_login(self, request, response):
        user = self.user.login(**request.media)
        response.set_header('auth_token', user.id)
        response.media = {
            'id': user.id,
        }

    @join_point
    def on_post_register(self, request, response):
        self.user.add_user(**request.media)
        user = self.user.login(**request.media)
        response.set_header('auth_token', user.id)
        response.media = {
            'id': user.id,
        }


@component
class Chat:
    chat: services.Chat

    @join_point
    def on_get_show_info(self, request, response):
        token = request.headers['AUTH-TOKEN']
        chat = self.chat.get_info(token, **request.params)
        response.media = {
            'id': chat.id,
            'title': chat.title,
            'owner': chat.owner,
            'info': chat.info,
        }

    @join_point
    def on_get_show_users(self, request, response):
        token = request.headers['AUTH-TOKEN']
        users = self.chat.get_users(token, **request.params)
        response.media = {"users": str(users)}

    @join_point
    def on_post_add_chat(self, request, response):
        self.chat.add_chat(
            request.headers['AUTH-TOKEN'],
            **request.media,
        )
        response.media = {
            'message': 'Чат был создан'
        }

    @join_point
    def on_post_add_user(self, request, response):
        self.chat.add_user(
            request.headers['AUTH-TOKEN'],
            **request.media,
        )
        response.media = {
            'message': 'Пользователь был добавлен'
        }

    @join_point
    def on_post_modify_chat(self, request, response):
        self.chat.modify_chat(request.headers['AUTH-TOKEN'], **request.media)
        response.media = {
            'message': 'Чат был изменён'
        }

    @join_point
    def on_post_delete_chat(self, request, response):
        self.chat.delete_chat(request.headers['AUTH-TOKEN'], **request.media)
        response.media = {
            'message': 'Чат был удалён'
        }

    @join_point
    def on_post_join_chat(self, request, response):
        self.chat.join_chat(request.headers['AUTH-TOKEN'], **request.media)
        response.media = {
            'message': 'Вы присоединились к чату или уже состоите в нём'
        }

    @join_point
    def on_post_leave_chat(self, request, response):
        self.chat.leave_chat(request.headers['AUTH-TOKEN'], **request.media)
        response.media = {
            'message': 'Вы вышли из чата'
        }


@component
class Message:
    message: services.Message

    @join_point
    def on_post_write_message(self, request, response):
        self.message.write_message(request.headers['AUTH-TOKEN'], **request.media)
        response.media = {
            'message': 'Сообщение успешно отправлено'
        }

    @join_point
    def on_get_messages(self, request, response):
        token = request.headers['AUTH-TOKEN']
        messages = self.message.get_message(token, **request.params)
        response.media = {"messages": str(messages)}
