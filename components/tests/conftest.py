import pytest
from unittest.mock import Mock
import datetime

from components.chat_backend.chat.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def chat():
    return dataclasses.Chat(
        id=1,
        title='Title',
        info='Info',
        owner=1
    )


@pytest.fixture(scope='function')
def chat_user():
    return dataclasses.ChatUser(
        id=1,
        user=1,
        chat=1,
    )


@pytest.fixture(scope='function')
def user():
    return dataclasses.User(
        id=1,
        username='alex',
        password='qwerty',
    )


@pytest.fixture(scope='function')
def chats_repo(chat):
    chats_repo = Mock(interfaces.ChatsRepo)
    chats_repo.add = Mock(return_value=chat)
    chats_repo.get_by_id = Mock(return_value=chat)

    return chats_repo


@pytest.fixture(scope='function')
def chat_user_repo(chat_user):
    chat_user_repo = Mock(interfaces.ChatUsersRepo)
    chat_user_repo.get_by_id = Mock(return_value=chat_user)
    return chat_user_repo


@pytest.fixture(scope='function')
def message_repo(chat):
    message_repo = Mock(interfaces.MessageRepo)
    return message_repo


@pytest.fixture(scope='function')
def user_repo(user):
    user_repo = Mock(interfaces.UsersRepo)
    chat_user_repo.add = Mock(return_value=user)
    return user_repo
