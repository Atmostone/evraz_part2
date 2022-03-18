from typing import Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from components.chat_backend.application.dataclasses import User
from components.chat_backend.application.interfaces import UsersRepo


@component
class UsersRepo(BaseRepository, UsersRepo):
    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, customer: User):
        self.session.add(customer)
        self.session.flush()

        return customer
