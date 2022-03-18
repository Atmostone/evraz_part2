from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    DateTime
)

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
)

chat = Table(
    'chat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('info', String, nullable=True),
    Column('owner', ForeignKey('user.id'), nullable=False),
)

chat_user = Table(
    'chat_user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('info', String, nullable=True),
    Column('owner', ForeignKey('user.id'), nullable=False),
)

message = Table(
    'message',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String, nullable=True),
    Column('chat', ForeignKey('chat.id'), nullable=False),
    Column('user', ForeignKey('user.id'), nullable=False),
    Column('datetime', DateTime, nullable=False),
)