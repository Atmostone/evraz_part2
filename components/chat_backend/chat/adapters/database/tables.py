from sqlalchemy import (
    Column,
    Float,
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
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False)
)

chat = Table(
    'chat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('info', String, nullable=True),
    Column('owner', ForeignKey('User'), nullable=False)
)

chat_user = Table(
    'chat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('info', String, nullable=True),
    Column('owner', ForeignKey('User'), nullable=False)
)

message = Table(
    'chat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String, nullable=True),
    Column('chat', ForeignKey('Chat'), nullable=False),
    Column('user', ForeignKey('User'), nullable=False),
    Column('datetime', DateTime, nullable=False),
)