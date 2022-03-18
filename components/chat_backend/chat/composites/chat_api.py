
from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from components.chat_backend.chat.adapters import database, chat_api


from wsgiref.simple_server import make_server

from components.chat_backend.chat.adapters.database import repositories
from components.chat_backend.chat.application import services


class Settings:
    db = database.Settings()
    shop_api = chat_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = repositories.UsersRepo(context=context)
    chats_repo = repositories.ChatsRepo(context=context)


class Application:
    user = services.User(users_repo=DB.users_repo)
    chat = services.Chat(chats_repo=DB.chats_repo)

    is_dev_mode = Settings.shop_api.IS_DEV_MODE
    allow_origins = Settings.shop_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    chat_api.join_points.join(DB.context)


app = chat_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    user=Application.user,
    chat=Application.chat,
)

with make_server('', 8000, app) as server:
    print(f'Server running on http://localhost:{server.server_port} ...')
    server.serve_forever()

