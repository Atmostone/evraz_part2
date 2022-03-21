from dataclasses import asdict

import pytest

from build.lib.components.application.dataclasses import Chat
from components.chat_backend.chat.application import services


@pytest.fixture(scope='function')
def chat_test(chats_repo, chat_user_repo):
    return services.Chat(
        chats_repo=chats_repo,
        chat_user_repo=chat_user_repo,
    )


@pytest.fixture(scope='function')
def chat_user_test(chats_repo, chat_user_repo):
    return services.Chat(
        chats_repo=chats_repo,
        chat_user_repo=chat_user_repo,
    )


@pytest.fixture(scope='function')
def message_test(chats_repo, chat_user_repo, message_repo):
    return services.Message(
        chats_repo=chats_repo,
        chat_user_repo=chat_user_repo,
        message_repo=message_repo
    )


@pytest.fixture(scope='function')
def user_test(users_repo):
    return services.User(users_repo=users_repo)


test_data_chat = {
    'title': 'Title',
    'info': 'Info',
    'owner': 1,
}

test_data_chat_modify = {
    'title': 'Title2',
    'info': 'Info2',
    'token': 1,
    'owner': 1,
    'id': 1,
}

test_data_user_test = {
    'user': 1,
    'chat': 1,
}

test_data_user = {
    'username': 'alex',
    'password': 'qwerty',
}


def test_add_chat(chat_test):
    chat = chat_test.chats_repo.add_chat(**test_data_chat)
    chat_test.chats_repo.add_chat.assert_called_once()
    assert {'title': chat.title, 'info': chat.info, 'owner': chat.owner} == test_data_chat


def test_modify_chat(chat_test):
    chat = chat_test.add_chat(**test_data_chat)
    chat2 = chat_test.modify_chat(**test_data_chat_modify)
    assert {'title': chat2.title, 'info': chat2.info, 'owner': chat2.owner,
            'id': chat2.id, 'token': chat2.owner} == test_data_chat_modify


# def test_delete_chat(chat_test):
#     chat_test.chats_repo.add_chat(**test_data_chat)
#     chat_test.chats_repo.delete_chat(token=1, id=1)
#
#     print('!!!!!!!!!', chat_test.chats_repo.get_by_id(1), '!!!!!!!!!!!!!')

    assert chat_test.chats_repo.get_by_id(1)


def test_get_info(chat_test):
    chat = chat_test.chats_repo.add_chat(**test_data_chat)
    chat_info = chat_test.chats_repo.get_by_id(1)
    assert chat == chat_info


# def test_write_message(chat_test, message_test, chat_user_repo):
#     chat = chat_test.add_chat(**test_data_chat)
#     chat_user = chat_user_repo.get_info(1, 1)
#     print('==========', chat, '==================')
#     print('==========', chat_user, '==================')
#     message = message_test.write_message(**test_data_message)
#     assert message == test_data_message
#

def test_add_user(user_test):
    user = user_test.add_user(**test_data_user)
    assert {'username': user.username, 'password': user.password} == test_data_user


def test_login(user_test):
    user2 = user_test.users_repo.add_user(**test_data_user)
    user = user_test.users_repo.login(**test_data_user)
    assert user == user2


def test_get_users(chat_user_test):
    users = chat_user_test.chat_user_repo.get_users(**test_data_user_test)
    assert {'user': users.user, 'chat': users.chat} == test_data_user_test
