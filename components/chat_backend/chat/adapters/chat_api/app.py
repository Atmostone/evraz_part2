from typing import Tuple, Union

import falcon

from classic.http_api import App
from classic.http_auth import Authenticator
from classic.http_auth import strategies as auth_strategies

from . import auth, controllers
from ...application import services


def create_app(
        is_dev_mode: bool,
        allow_origins: Union[str, Tuple[str, ...]],
        user: services.User,
        chat: services.Chat,

) -> App:
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)

    if is_dev_mode:
        cors_middleware = falcon.CORSMiddleware(allow_origins='*')
        authenticator.set_strategies(auth.dummy_strategy)
    else:
        cors_middleware = falcon.CORSMiddleware(allow_origins=allow_origins)
        authenticator.set_strategies(auth_strategies.KeycloakOpenId())

    middleware = [cors_middleware]

    app = App(middleware=middleware, prefix='/api')

    app.register(controllers.User(user=user))
    app.register(controllers.Chat(chat=chat))

    return app
