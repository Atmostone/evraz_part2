from classic.components import component

from .join_points import join_point
from ...application import services


@component
class User:
    user: services.User

    @join_point
    def on_get_show_info(self, request, response):
        user = self.user.get_info(**request.params)
        response.media = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
        }

    @join_point
    def on_post_add_user(self, request, response):
        self.user.add_user(
            **request.media,
        )


@component
class Chat:
    chat: services.Chat

    @join_point
    def on_get_show_info(self, request, response):
        chat = self.chat.get_info(**request.params)
        response.media = {
            'id': chat.id,
            'owner': chat.owner,
            'info': chat.info,
        }

    @join_point
    def on_post_add_chat(self, request, response):
        self.chat.add_chat(
            **request.media,
        )
        response.media = {
            'message': 'Чат был создан'
        }

    @join_point
    def on_patch_modify_chat(self, request, response):
        self.chat.modify_chat(**request.media)
        response.media = {
            'message': 'Чат был изменён'
        }

