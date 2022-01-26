import sqlalchemy
from sqlalchemy import ForeignKey
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("fullname"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("type"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)


saving  = sqlalchemy.Table(
    "savings",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("saving_name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("income"     , sqlalchemy.Float),
    sqlalchemy.Column("currency"     , sqlalchemy.String),
    sqlalchemy.Column("target"    , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)