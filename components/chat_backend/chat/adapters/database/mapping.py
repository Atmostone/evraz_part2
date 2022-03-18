
from sqlalchemy.orm import registry

from . import tables
from ...application import dataclasses

mapper = registry()

mapper.map_imperatively(dataclasses.User, tables.user)
mapper.map_imperatively(dataclasses.Chat, tables.chat)