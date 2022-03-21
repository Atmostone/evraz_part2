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
def message_test(chats_repo, chat_user_repo, message_repo):
    return services.Message(
        chats_repo=chats_repo,
        chat_user_repo=chat_user_repo,
        message_repo=message_repo
    )


@pytest.fixture(scope='function')
def user_test(user_repo):
    return services.User(user_repo=user_repo)


test_data_chat = {
    'title': 'Title',
    'info': 'Info',
    'owner': 1,
}

test_data_message = {
    'token': 1,
    'chat_id': 1,
    'text': 'HELP ME!'
}

test_data_user = {
    'chat_id': 1,
    'text': 'HELP ME!'
}


def test_add_chat(chat_test):
    chat = chat_test.add_chat(**test_data_chat)
    chat_test.chats_repo.add.assert_called_once()
    assert {'title': chat.title, 'info': chat.info, 'owner': chat.owner} == test_data_chat


def test_get_info(chat_test):
    chat = chat_test.add_chat(**test_data_chat)
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

# def test_add_user(user_test):
#     user = user_test.add(username='Alex', password='qwerty')
#     assert {user['username'], user['password']} == test_data_user
